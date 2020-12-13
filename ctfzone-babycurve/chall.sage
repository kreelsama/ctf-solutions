from secret import a, b, p, flag
from Crypto.Util import number

assert len(flag) == 36
assert all(map(is_prime, [a, b, p]))

E = EllipticCurve(Zmod(p), [a, b])
P = E((636441264789424866585476751229, 775421649189707161813344094607))

enc = map(lambda x: x*P, map(number.bytes_to_long, [flag[12*i:12*(i+1)] for i in range(3)]))
for item in enc: 
    print(item)