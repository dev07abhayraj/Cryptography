#  Write a Python code to encrypt 'test.jpeg' using AES encryption ?

import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding

# Generate a random key and IV
def generate_key_iv(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)
    iv = os.urandom(16)
    return key, iv

# Encrypt the file
def encrypt_file(input_file, output_file, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()

    with open(input_file, 'rb') as f:
        file_data = f.read()

    padded_data = padder.update(file_data) + padder.finalize()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)  # Prepend IV for use in decryption

def main():
    password = b'my_strong_password'
    salt = os.urandom(16)  # You should save this salt to use during decryption
    key, iv = generate_key_iv(password, salt)

    input_file = 'test.jpeg'
    output_file = 'test_encrypted.jpeg'
    encrypt_file(input_file, output_file, key, iv)

    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")

if __name__ == "__main__":
    main()
