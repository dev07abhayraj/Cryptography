#  Write a program to convert the string 'crypto world' to a hash using the sha3_256 hashing algorithm ?

import hashlib
print(hashlib.sha3_256(b'crypto world').hexdigest())