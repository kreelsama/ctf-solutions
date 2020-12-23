import os,signal
from flag import FLAG

signal.alarm(600)
assert(FLAG.startswith("0ops{"))
assert(FLAG.endswith("}"))

def xor(a,b):
    assert(len(a)==len(b))
    c = ""
    for i in range(len(a)):
        c+=chr(ord(a[i])^ord(b[i]))
    return c

def encrypt(data):
    key = os.urandom(len(data))
    return xor(data,key)

print "welcome to sssssssssssssupper safe stream cipher"
while True:
    data = raw_input("input your data:").strip()
    data = FLAG+data
    data = data.encode("zlib")
    data = encrypt(data)
    print data.encode("hex")

