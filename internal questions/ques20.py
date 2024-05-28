#  Write a program to convert the string 'cryptography' to a hash using the shake_256 hashing algorithm ?

import hashlib 

print(hashlib.shake_256(b'cryptography').hexdigest(20))