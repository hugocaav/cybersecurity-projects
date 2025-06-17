# This is the main routine of the script.
# It generates a new encryption key, encrypts a text file, and then decrypts it back.
# Useful for demonstrating how symmetric file encryption works in real life.

from cryptography.fernet import Fernet

# Generate or load a key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

# Encrypt a file
def encrypt_file(filename, key):
    with open(filename, "rb") as file:
        data = file.read()

    encrypted = Fernet(key).encrypt(data)

    with open(filename + ".enc", "wb") as file:
        file.write(encrypted)

# Decrypt a file
def decrypt_file(filename, key):
    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted = Fernet(key).decrypt(encrypted_data)

    with open("decrypted_" + filename.replace(".enc", ""), "wb") as file:
        file.write(decrypted)

# Main program
if __name__ == "__main__":
    generate_key()
    key = load_key()

    encrypt_file("secret.txt", key)
    decrypt_file("secret.txt.enc", key)