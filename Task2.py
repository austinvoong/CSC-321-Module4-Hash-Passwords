import nltk
# nltk.download('words')
import bcrypt
import time
from nltk.corpus import words

word_list = words.words() #Load word corpus
#Filter the word list for words between lengths of 6 and 10
filtered_words = [word.lower() for word in word_list if 6 <= len(word) <= 10]

#Crack password function
def crack_password(user_line):
    # "User:$Algorithm$Workfactor$SaltHash"
    user_parts = user_line.split(':') # Splits into User and $Algorithm$Workfactor$SaltHash
    username = user_parts[0].strip()
    bcrypt_hash = user_parts[1].strip()
    
    print(f"Cracking password for user: {username}")
    start_time = time.time()

    for password in filtered_words:
        print(f"User: {username} {password}")

        try:
            if bcrypt.checkpw(password.encode('utf-8'), bcrypt_hash.encode('utf-8')):
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Password for {username} cracked: {password} \n Elapsed time: {elapsed_time:.2f} seconds)")
                return username, password, elapsed_time
        except Exception as e:
            print(f"Error, user: {username}, password: {password}: {str(e)}")
        
    return username, None, None

# Crack shadow file function
def shadow_file(sf):
    results = []
    with open(sf, 'r') as f:
        for line in f.readlines():
            if line.strip():
                results.append(crack_password(line.strip()))
    return results

sf = 'shadow_file.txt'
cracked_passwords = shadow_file(sf)

for username, password, elapsed_time in cracked_passwords:

    if password:
        print(f"User: {username}, Password: {password}, Elapsed time: {elapsed_time:.2f} seconds")
    else:
        print(f"User: {username}, Password not cracked")
