#! /usr/bin/env python3
import bs4
from urllib.request import urlopen


def download_tables():
    print('Downloading droptables...')
    try:
        droptables = urlopen('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    except:
        print('Downloading failed!\nTrying again in 5 minutes')
        return None
    print('Processing droptables...')
    droptables = bs4.BeautifulSoup(droptables, 'html5lib')
    return droptables

def define_input_type(item):
    mods = []
table = download_tables()
for i in table.select(''):
    print(i.getText())
