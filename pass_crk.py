import itertools
import time
import os

def brute_force_crack(password, charset):
    """
    Brute force password cracker using systematic combination generation.
    """
    length = len(password)
    total_combinations = len(charset) ** length
    print(f"Password length: {length}")
    print(f"Charset size: {len(charset)}")
    print(f"Total possible combinations: {total_combinations}")
    print("Note: Brute force is impractical for passwords longer than 8 characters.\n")

    if length > 8:
        print("Warning: This may take a very long time or be impossible for long passwords.")
        confirm = input("Continue? (y/n): ")
        if confirm.lower() != 'y':
            return None

    start_time = time.time()
    attempts = 0

    for combo in itertools.product(charset, repeat=length):
        attempts += 1
        guess = ''.join(combo)
        if attempts % 100000 == 0:  # Progress update every 100k attempts
            elapsed = time.time() - start_time
            print(f"Attempts: {attempts}, Time elapsed: {elapsed:.2f}s")
        if guess == password:
            elapsed = time.time() - start_time
            print(f"\nPassword cracked in {attempts} attempts and {elapsed:.2f} seconds!")
            return guess

    print("Password not found in all combinations. This shouldn't happen if charset is correct.")
    return None

# Define the character set
charset = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?"]

# Get password from user
password = input("Enter the password to crack: ")

# Check if password contains only characters in charset
if not all(c in charset for c in password):
    print("Error: Password contains characters not in the charset.")
    exit(1)

# Run the cracker
result = brute_force_crack(password, charset)
if result:
    print(f"The password is: {result}")
else:
    print("Failed to crack the password.")
