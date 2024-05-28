import hashlib as abhay

print("-------------------------------------------------")
print(abhay.algorithms_available) 
print("-------------------------------------------------")
print(abhay.algorithms_guaranteed)
print("-------------------------------------------------")


print(abhay.md5(b'Abhayraj').hexdigest())
print(abhay.sha1(b'Abhayraj').hexdigest())
print(abhay.sha256(b'Abhayraj').hexdigest())
print(abhay.sha3_224(b'Abhayraj').hexdigest())
print(abhay.blake2s(b'Abhayraj').hexdigest())
print(abhay.sha384(b'Abhayraj').hexdigest())
print(abhay.sha3_256(b'Abhayraj').hexdigest())
print(abhay.blake2b(b'Abhayraj').hexdigest())
print("-------------------------------------------------")


# Output

# a8f8df4329802067e14cfda89599052b
# e4855b94f23c9cbf321b638d3f1e2ec5ecc51587
# f6b4b132a9c0ded8943ebbca9bbc16521fffb8bbd0f91bc53d6f21fd705de5eb
# 3c581f01d2cd0a094b0b70158880a10c91e799a08ab5a96ddeae537f
# 47750caca7d59c7546cf1f9ae7d5ce4dba246f018f7e52960d665c0b81518ad6
# 3460cc4725804f234ff00b48da3922a998c5ef038e61eb483d1deb63a05055531be31e69e2ce398f5ccd46556898f86b
# cb089b212120df19bdce950a94130091316563e3cef788b65515226afd8d7291
# bfe03827878bc80f3d54b83636cad8f732f05aac0134f02243efb1afb8fa1cd45b3fc3edc7a8503f7f749e92698d7b9c3ca1935d70d9437f994a0772cb53f3be