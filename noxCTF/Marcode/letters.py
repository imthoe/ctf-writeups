import requests
from bs4 import BeautifulSoup

links = open('unique_links.txt').read().split()

for link in links:
    r = requests.get(link)
    soup = BeautifulSoup(r.text, 'html.parser')
    print (soup.title)
