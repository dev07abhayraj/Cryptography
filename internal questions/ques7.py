#  Write a program to convert the string 'hello world' to a hash using the sha3_512 hashing algorithm

import hashlib 

print(hashlib.sha3_512(b'hello World').hexdigest())
