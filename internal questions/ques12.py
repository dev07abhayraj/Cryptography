#  Write a program to convert the string '128 hashing' to a hash using the shake_128 hashing algorithm?

import hashlib
print(hashlib.shake_128(b'128 hashing').hexdigest(20))