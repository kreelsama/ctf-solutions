from Crypto.Util import number
from secret import flag

flag = number.bytes_to_long(flag)
P = number.getPrime(1024)
F.<x> = PolynomialRing(GF(P))

poly0 = F.irreducible_element(1337)
poly1 = F.irreducible_element(1361)
nonce0 = randint(0, P)
nonce1 = randint(0, P)
output0 = poly0(flag+nonce0)
output1 = poly1(flag+nonce1)

print(P)
print(nonce0, nonce1)
print(output0, output1)
print(poly0)
print(poly1)
