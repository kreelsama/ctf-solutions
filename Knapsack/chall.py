from hashlib import sha1
import random
import gmpy2
from flag import FLAG
from Crypto.Util.number import bytes_to_long

class Knapsack():
    def __init__(self,n):
        self.n = n
        self.makeKey(n)

    def encrypt(self,msgbit):
        enc = 0
        for i in range(self.n):
            if msgbit[i]=="1":
                enc+=self.pubKey[i]
        return enc

    def makeKey(self,n):
        privKey = [random.randint(1, 4**n)]
        s = privKey[0]
        for i in range(1,n):
            privKey.append(random.randint(s+1, 4**(n+i)))
            s += privKey[i]
        q = random.randint(s+1, 2*s)
	r = random.randint(1, q)
	while gmpy2.gcd(r, q) != 1:
		r = random.randint(1, q)
	self.pubKey = [ r*w % q for w in privKey ]

    def getpubKey(self):
        return self.pubKey

msgbit = bin(bytes_to_long(FLAG))[2:]
knapsack = Knapsack(len(msgbit))
enc = knapsack.encrypt(msgbit)
print enc
print knapsack.getpubKey()
