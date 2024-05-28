#  Write a program to convert the string 'cryptography' to a hash using the SHA-512 hashing algorithm?

import hashlib

print(hashlib.sha512(b'cryptography').hexdigest())