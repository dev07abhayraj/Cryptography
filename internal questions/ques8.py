#  Write a program to convert the string 'black2b hash' to a hash using the blake2b hashing algorithm?

import hashlib 

print(hashlib.blake2b(b'black2b hash').hexdigest())
