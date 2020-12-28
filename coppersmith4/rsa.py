from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long
import os
from flag import FLAG

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3

prefix = os.urandom(210)
salt = bytes_to_long(os.urandom(13))
plain1 = bytes_to_long(prefix+FLAG)
plain2 = plain1^salt


c1 = pow(plain1, e, n)
c2 = pow(plain2, e, n)

with open('enc.txt', 'wb') as f:
    f.write("n = "+str(n)+"\n")
    f.write("c1 = "+str(c1)+"\n")
    f.write("c2 = "+str(c2)+"\n")
