from pwn import *
import re

r = remote('34.216.132.109', 9093)
text = r.recv()
print(text)
letters = re.findall("'(.+?)'",text)
numbers = re.findall(r'\d{1,9}',text)


string = ''
string += letters[0]*int(numbers[0])
string += letters[1]*int(numbers[1])

payload = string+str(ord(letters[0])+ord(letters[1]))

print("PAYLOAD: "+payload)
r.sendline(payload)
ans = r.recv()
print(ans)

# The flag is: CodefestCTF{1_s33_y0u_4r3_a_m4n_0f_sp33d}
