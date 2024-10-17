import random, string, time
from Crypto.Hash import SHA256
import matplotlib.pyplot as plt

#Function to calculate the SHA256 hash
def sha256_hash(input_str):
    input_bytes = input_str.encode() #Convert input string to bytes
    hash = SHA256.new()
    hash.update(input_bytes) #Conver byte input string to hash
    return hash.hexdigest() #Return as a hexdecimal string

#Function to truncate hash
def truncate_hash(hash_string, bits):
    truncated = hash_string[:bits // 4] # Takes the first bit/4 chars of the hash string
    truncated_int = int(truncated, 16) #Convert substring to int
    bitmask = (1 << bits) - 1 #Creates bitmask
    return truncated_int & bitmask #returns bitwise "and" between int and bitmask

#Helper function to calculate Hamming Distance
def hamming_distance(str1, str2):
    count = 0
    for char1, char2 in zip(str1, str2): #
        if char1!= char2:
            count += 1
    return count

#Function to return hamming distance of 1
def find_hamming_distance_1():
    #Generate a random string 'base' of 10 ascii letters
    base = ''.join(random.choices(string.ascii_letters, k = 10)) 
    for i in range(len(base)):
        #Flip the i-th bit of base
        modified = base[:i] + (chr(ord(base[i]) ^ 1)) + base[i + 1:] 
        if hamming_distance(base, modified) == 1:
            return base, modified
    return None, None

#Function to find collisions for truncated hashes
def find_collision(bits, max_attempts):
    seen = {}
    start_time = time.time()
    for attempt in range(1, max_attempts + 1):
        s = ''.join(random.choices(string.ascii_letters, k = 10))
        truncated_hash = truncate_hash(sha256_hash(s), bits)
        if truncated_hash in seen:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return seen[truncated_hash], s, attempt, elapsed_time
        else:
            seen[truncated_hash] = s
    return None, None, max_attempts, time.time() - start_time

def task_1a():
    print("Task1a: SHA256 hashes of random inputs")
    for input_str in ["HELLO", "THIS IS A test", "abc123"]:
        print(f"Input: {input_str} -> SHA256 Hash: {sha256_hash(input_str)}")

def task_1b():
    print("\nTask1b: Strings with Hamming distance of 1")
    for _ in range (3):
        str1, str2 = find_hamming_distance_1()
        if str1 and str2:
            print(f"String 1: {str1}, Hash 1: {sha256_hash(str1)}")
            print(f"String 2: {str2}, Hash 2: {sha256_hash(str2)}\n")

#Task 1c: Finding collisions for truncated hashes
def task_1c():
    print("Task 1c: Finding collisions for truncated hashes")
    bits_list = []
    time_list = []
    inputs_list = []
    
    for bits in range(8, 51, 2):
        input1, input2, attempts, elapsed_time = find_collision(bits, 100000)
        if input1 and input2:
            bits_list.append(bits)
            time_list.append(elapsed_time)
            inputs_list.append(attempts)
            print(f"Collision found for {bits} bits: {input1} & {input2} in {elapsed_time:.2f}s after {attempts} attempts")
        else:
            print(f"TIMEOUT: No collision found for {bits} bits after {attempts} attempts")
    
    # Plotting results
    plt.figure(figsize=(12, 6))
    #Plot1
    plt.subplot(1, 2, 1)
    plt.plot(bits_list, time_list, marker='o')
    plt.title('Digest Size vs Collision Time')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Time (seconds)')

    #Plot2
    plt.subplot(1, 2, 2)
    plt.plot(bits_list, inputs_list, marker='o')
    plt.title('Digest Size vs Number of Inputs')
    plt.xlabel('Digest Size (bits)')
    plt.ylabel('Number of Inputs')

    plt.tight_layout()
    plt.savefig('collision_analysis.png')
    plt.show()

# #Test: hash simple strings
# inputs = ["example1", "example2", "example3"]
# for inp in inputs:
#     print(f"Input: {inp} -> SHA256 Hash: {sha256_hash(inp)}")
def main():
    task_1a()
    task_1b()
    task_1c()

if __name__ == "__main__":
    main()