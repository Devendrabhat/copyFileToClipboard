try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
from bs4 import BeautifulSoup as bs
import re
import os


# From link
link = input("Enter the website link to find out mail ids => ")
page = urlopen(link)

# From file
# page = open('trial.txt', 'r')

soup = bs(page, 'html.parser')
mailids = set()
for a in soup.find_all('a'):
    mainid = a.get('rel')
    if mainid != None and re.search(r'@ubisoft.com', mainid[0]):
            mailids.add(mainid[0])
string = ''
for line in mailids:
    string = string+line+' '
print(string)
os.system("echo {} | clip".format(string))
print("Done, Now do ctrl+v somewhere.")
