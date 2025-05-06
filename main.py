import hashlib
import itertools

attempts = 0


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force(target_hash, characters, attempts):
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




if __name__ == "__main__":
    target_hash = input("Please enter a hashed password:\n")
    
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"£$%^&*()_+-=[]#{}~:;@<>?,./|\¬`'
    
    result = brute_force(target_hash, characters, attempts)
    pswdfile = "C:\\Users\\jackw\\python\\crackedpasswords.txt"
    file = open(pswdfile, "a")
    file.write(result)
    file.close()
    
    if result:
        print(f"Password found: {result}")
    else:
        print("Password not found.")
