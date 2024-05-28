#  Write a program to convert the string 'sha hash' to a hash using the sha256 hashing algorithm?

import hashlib 

print(hashlib.sha256(b'Hello World').hexdigest())
