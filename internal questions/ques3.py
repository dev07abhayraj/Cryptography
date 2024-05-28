  
# 3. Write a program to convert the string 'MD5 HASH' to a hash using the md5 hashing algorithm?

import hashlib 

print(hashlib.md5(b'Hello World').hexdigest())

