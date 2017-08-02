import bs4
from urllib.request import urlopen


def download_tables():
    print('Downloading droptables...')
    try:
        with open('table of mods') as t:
            droptables = t.read()

    except:
        print('Downloading failed!\nTrying again in 5 minutes')
        return None
    print('Processing droptables...')
    droptables = bs4.BeautifulSoup(droptables, 'html5lib')
    print(droptables.prettify())
    return droptables


table = download_tables()
for i in table.select('tr'):
    #print(i.colspan)
    if i.has_attr('class'):
        continue

print(mods)