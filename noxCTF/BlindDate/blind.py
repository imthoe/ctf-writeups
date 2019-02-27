f = open('BlindDate.jpeg', "rb")
s = f.read()
f.close()

data = ''
for i in range(0,len(s),4):
    data += s[i:i+4][::-1]

nf = open('blind.jpeg','wb')
nf.write(data)
