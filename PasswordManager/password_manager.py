from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import hashlib
import getpass

'''def write_salt():
    import os
    salt = os.urandom(16)
    with open('salt.key', 'wb') as salt_file:
        salt_file.write(salt)

write_salt()'''

def load_salt():
    with open('salt.key', 'rb') as f:
        return f.read()

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

# Hashed master password (hash of "hello123")
# To generate: hashlib.sha256("hello123".encode()).hexdigest()
MASTER_PASSWORD_HASH = "27cc6994fc1c01ce6659c6bddca9b69c4c6a9418065e612c69d110b3f7b11f8a"

main_pwd = getpass.getpass("What is the main password? ")

# Verify master password
pwd_hash = hashlib.sha256(main_pwd.encode()).hexdigest()
if pwd_hash != MASTER_PASSWORD_HASH:
    print("Incorrect password. Access denied.")
    exit()

# Load salt and derive encryption key
salt = load_salt()
key = derive_key(main_pwd, salt)
fer = Fernet(key)



def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            try:
                decrypted_pwd = fer.decrypt(passw.encode()).decode()
                print(f"User: {user} | Password: {decrypted_pwd}")
            except Exception as e:
                print(f"User: {user} | Error decrypting password: {e}")

def add():
    name = input("Enter the user name: ")
    pwd = getpass.getpass("Enter the password: ")

    with open('passwords.txt','a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + '|' + encrypted_pwd + '\n')
        print("Password added successfully.")

while True:
    mode = input("Would you like to view and existing password or add a new password? (view/add) or type 'q' to exit: ").lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print("Invalid mode.")
        continue
