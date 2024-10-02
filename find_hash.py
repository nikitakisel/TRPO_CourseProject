import hashlib
print(str(int(hashlib.md5(input().encode()).hexdigest(), 16)))
