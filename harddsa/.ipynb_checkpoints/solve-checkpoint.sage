from hashlib import sha1
from Crypto.Util.number import *
p = 89884656743115795389374444357965596041707103579335619241165156429225502365521439025499103971147870579637910013872240481446642759865727715143856448882853102298215102584779112052046581658273396430166671654945955572937243406324990511517175949775424708250369373972195526071010722126994053027079640824789677194681
q = 838114989280207343931101099984559960927246139967
g = 81276779940548524670494254192706613917067069432886996156070646492653656558343240172021379272918460788370332639784438273863095242075038574780575863033117339765921362764295832142292157994542582821081221019750571423117394603653210942993984937508928164068015833890842969704124928271625205241823140934184765854933
Rp = Integers(p)
Rq = Integers(q)

m = []
r = []
s = []
with open('sign', 'rb') as f:
    for line in f.readlines():
        m.append(Integer(line.split(b' ')[0], 16))
        r.append(Integer(line.split(b' ')[1]))
        s.append(Integer(line.split(b' ')[2]))

h = [Integer(sha1(long_to_bytes(mi)).hexdigest(), 16) for mi in m]

n = len(m)
l = 256
U = vector([(-h[i])*inverse_mod(256*s[i], q)%q for i in range(n)])
T = vector([r[i]*inverse_mod(256*s[i], q) % q for i in range(n)])
Q = q*matrix.identity(n)
vT = vector([0 for _ in range(n + 2)])
vU = vector([0 for _ in range(n + 2)])
sT = 1
sU = 1
vT[-2] = sT
vU[-1] = sU

M = Q.stack(T).stack(U).augment(vT).augment(vU)

B = M.LLL()

x = 1
for i,v in enumerate(B):
    if v[-1] == sU:
        x = Rq(-v[-2] / sT)
        break

print(B)

# for each in 