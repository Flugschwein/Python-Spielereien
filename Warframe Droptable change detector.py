import requests, bs4


def download_tables():
    droptables = requests.get('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    droptables = bs4.BeautifulSoup(droptables)
    return droptables