from urllib.request import urlopen
import bs4
import pprint
droptables = urlopen('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
droptables = bs4.BeautifulSoup(droptables, 'html.parser')
pprint.pprint(droptables.find_all('a'))