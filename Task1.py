# import random, string, time
from Crypto.Hash import SHA256
# import matplotlib.pyplot as plt

def sha256_hash(input_str):
    input_bytes = input_str.encode()
    hash = SHA256.new()
    hash.update(input_bytes)
    return hash.hexdigest()

def task_1a():
    print("Task1a: SHA256 hashes of random inputs")
    for input_str in ["HELLO", "THIS IS A test", "abc123"]:
        print(f"Input: {input_str} -> SHA256 Hash: {sha256_hash(input_str)}")

# #Test: hash simple strings
# inputs = ["example1", "example2", "example3"]
# for inp in inputs:
#     print(f"Input: {inp} -> SHA256 Hash: {sha256_hash(inp)}")
def main():
    task_1a()
if __name__ == "__main__":
    main()