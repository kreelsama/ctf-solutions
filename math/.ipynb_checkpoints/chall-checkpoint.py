from Crypto.Util import number
from secret import flag
assert len(flag) == 32

m = number.bytes_to_long(flag)
p = number.getPrime(1024)
q = number.getPrime(1024)
n = p * q
a = n * number.getRandomRange(0, 1 << 1800) + 1
b = number.getRandomRange(0, n)
c = pow(a, m, n**2) * pow(b, n, n**2) % (n**2)

print(f"n = {n}")
print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")