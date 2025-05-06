import hashlib
import itertools
from pathlib import Path


CHARACTER_SET = (
    'abcdefghijklmnopqrstuvwxyz'
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    '0123456789'
    '!"£$%^&*()-=_+[]#{}~;:@,./<>?|\\¬`'
)

OUTPUT_FILE = Path("cracked_passwords.txt")




def hash_password(password):
    # Returns SHA-256 of given password
    return hashlib.sha256(password.encode()).hexdigest()


def brute_force(target_hash, characters):
    # Attempts to brute-force SHA-256 using character set
    attempts = 0
    length = 1

    while True:
        for combination in itertools.product(characters, repeat=length):
            password = ''.join(combination)
            hashed_password = hash_password(password)

            attempts += 1
            print(f"Trying password: {password}\nAttempt:{attempts}\n")

            if hashed_password == target_hash:
                return password

        length += 1


def save_cracked_passwords(password):
    # Appends the cracked password to a file
    with OUTPUT_FILE.open("a", encoding="utf-8") as file:
        file.write(password + "\n")


def main():
    target_hash = input("Enter the SHA-256 hash to crack:\n").strip()

    print("Beginning brute-force...")
    cracked_password = brute_force(target_hash, CHARACTER_SET)

    if cracked_password:
        print(f"Password found: {cracked_password}")
        save_cracked_passwords(cracked_password)
    else:
        print("ERROR")




if __name__ == "__main__":
    main()
