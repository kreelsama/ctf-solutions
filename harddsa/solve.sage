from hashlib import sha1
from Crypto.Util.number import *

p = 89884656743115795389374444357965596041707103579335619241165156429225502365521439025499103971147870579637910013872240481446642759865727715143856448882853102298215102584779112052046581658273396430166671654945955572937243406324990511517175949775424708250369373972195526071010722126994053027079640824789677194681
q = 838114989280207343931101099984559960927246139967
g = 81276779940548524670494254192706613917067069432886996156070646492653656558343240172021379272918460788370332639784438273863095242075038574780575863033117339765921362764295832142292157994542582821081221019750571423117394603653210942993984937508928164068015833890842969704124928271625205241823140934184765854933


m = []
r = []
s = []
with open('sig', 'rb') as f:
    for line in f.readlines():
        m.append(Integer(line.split(b' ')[0], 16))
        r.append(Integer(line.split(b' ')[1]))
        s.append(Integer(line.split(b' ')[2]))

h = [Integer(sha1(long_to_bytes(mi)).hexdigest(), 16) for mi in m]

n = len(m)
print(n)
l = 256

sT = 1 / l
sU = q*sT


M = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(n):
    M[i][i] = q

for i in range(n):
    M[n][i] = r[i]*inverse_mod(l*s[i], q) % q 

for i in range(n):
    M[n+1][i] = (-h[i])*inverse_mod(l*s[i], q)%q

M[n][n] = sT
M[n+1][n+1] = sU

M = matrix(M)

B = M.LLL()

x = 1
for i,v in enumerate(B):
    if v[-1] == sU:
        x = -v[-2] / sT % q
        for i in range(n):
            k = (h[i] + x*r[i]) / s[i] % q
            print(hex(k%256)[2:], end=' ')
            
            if k%l : break
        else: 
            print(x)
            print("0ops{"+hex(x)[2:].strip("L")+"}")
            break

    # print(B)