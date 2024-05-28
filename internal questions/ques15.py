#  Write a program to convert the string 'crypto' to a hash using the sha3_384 hashing algorithm ?

import hashlib
print(hashlib.sha3_384(b'crypto').hexdigest())