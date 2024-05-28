#  Write a program to convert the string 'sha1 hash' to a hash using the sha1 hashing algorithm ?

import hashlib
print(hashlib.sha1(b'sha1 hash').hexdigest())