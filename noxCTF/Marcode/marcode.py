from pyzbar.pyzbar import decode
from PIL import Image
import sys

links = open('unique_links.txt').read().split('\n')
text = 'THE_WOMNAPRDUF?YSILCQGZBKXVJ'
solution = ''

for i in range(1,3491):
    l = decode(Image.open('frames/frame-'+str(i).zfill(4)+'.png'))[0].data
    for x in range(len(links)):
        if l == links[x]:
            solution += text[x]
            
print solution
