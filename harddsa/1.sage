import hashlib
from Crypto.Util.number import *
p = 89884656743115795389374444357965596041707103579335619241165156429225502365521439025499103971147870579637910013872240481446642759865727715143856448882853102298215102584779112052046581658273396430166671654945955572937243406324990511517175949775424708250369373972195526071010722126994053027079640824789677194681L
q = 838114989280207343931101099984559960927246139967L
Rp = Integers(p)
Rq = Integers(q)
g = Rp(81276779940548524670494254192706613917067069432886996156070646492653656558343240172021379272918460788370332639784438273863095242075038574780575863033117339765921362764295832142292157994542582821081221019750571423117394603653210942993984937508928164068015833890842969704124928271625205241823140934184765854933L)

# The DSA algorithm involves two rings: the integers modulo p and the integers modulo q
Rp = Integers(p)
Rq = Integers(q)


def get_hash(cmd):
  return int(hashlib.sha1(long_to_bytes(cmd)).hexdigest(), 16)


msb = False # modify exploit to work for variant problem where most sig. byte is 0

h = []
rs_pairs = []
with open('sign', 'r') as f:
  for line in f:
    m, r, s = line.strip().split(' ')
    r, s = Rq(int(r)), Rq(int(s))
    rs_pairs.append((r,s))
    h.append(get_hash(Integer(m, 16)))


# Construct lattice
n = len(h) # This can be as low as 66 for the original problem, or 78 for the MSB variant
rs_pairs = rs_pairs[:n]
L = pow(2, 8)
if msb:
  L = 1

T = vector([int(r  / (L * s)) for (r, s) in rs_pairs])
U = vector([int(-h[i] / (L * rs_pairs[i][1])) for i in range(n)])
Q = q * matrix.identity(n)

sT = 1
sU = 1
vT = vector([0 for _ in range(n + 2)])
vU = vector([0 for _ in range(n + 2)])
vT[-2] = sT
vU[-1] = sU

'''
        [           | |   | ]
        [    q*I    | 0   0 ]
        [           | |   | ]
    M = [-----------+-------]
        [ --- T --- | sT  0 ]
        [ --- U --- | 0  sU ]
'''

M = Q.stack(T).stack(U).augment(vT).augment(vU)
B = M.LLL()

x = 1
for i, v in enumerate(B):
  if v[-1] == sU:
    x = Rq(-v[-2] / sT)
    break

print(x)