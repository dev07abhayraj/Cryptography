#  Write a program to convert the string 'crypto world' to a hash using the sha3_224 hashing algorithm?


import hashlib
print(hashlib.sha3_224(b'crypto world').hexdigest())