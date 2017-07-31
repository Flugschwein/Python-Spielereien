import bs4
from urllib.request import urlopen


def download_tables():
    droptables = urlopen('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    droptables = bs4.BeautifulSoup(droptables, 'html.parser')
    return droptables
print(download_tables().prettify())
