import urllib.request as req
from bs4 import BeautifulSoup as bs
import re

# link = input("Enter the website link to find out mail ids => ")
# page = req.urlopen(link)
page = open('trial.txt', 'r')
soup = bs(page, 'html.parser')

for a in soup.find_all('a'):
    mainid = a.get('rel')
    if mainid != None and re.search(r'@ubisoft.com', mainid[0]):
            print(mainid[0])
