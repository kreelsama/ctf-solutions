import os
from Crypto.Util import number
from secret import flag

p = number.getPrime(1024)
q = number.getPrime(1024)
n = p * q   
e = 65537

flag = os.urandom(255-len(flag)) + flag
flag = number.bytes_to_long(flag)
data = number.bytes_to_long(b"0ops")

enc_flag = pow(flag, e, n)
enc_data = pow(data, p, n)

print(f"n = {n}")
print(f"enc_flag = {enc_flag}")
print(f"enc_data = {enc_data}")