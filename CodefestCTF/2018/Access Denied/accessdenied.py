from pwn import *
import sys

codes = []
user = ""
for xy in range(0,1001):
    count_ = xy%1000    #User ID/ UID in the table is always positive

    generator = "xorshift"
    random.seed(generator)
    count = 0;

    for ch in user:
        ra = random.randint(1, ord(ch))
        rb = (ord(ch) * random.randint(1, len(user))) ^ random.randint(1, ord(ch))

        count += (ra + rb)/2

    code = 1

    for i in range(1,count+count_):
        code = (code + random.randint(1, i) ) % 1000000

    final = random.randint(1,9) * 1000000 + code
    codes.append(final)

r = remote('34.216.132.109',9094)
r.recvuntil("Enter your name: ")
r.sendline()

for x in codes:
    text = r.recv()
    if "flag" not in text:
        r.sendline(str(x))
    else:
        print(text)
        print(x)
        sys.exit()

# The flag is CodefestCTF{1_s33_y0u_4r3_a_m4n_0f_r4nd0mn3ss}
