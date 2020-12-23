from Crypto.Util.number import getPrime, bytes_to_long
import gmpy2
from flag import FLAG
import os

prefix = os.urandom(255-len(FLAG))
plain = bytes_to_long(prefix+FLAG)

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 3
c = pow(plain,e,n)
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
d = (d&(2**590-1))

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("c = "+str(c)+"\n")
    f.write("d = "+str(d)+"\n")
