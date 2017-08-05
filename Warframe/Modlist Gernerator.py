import bs4
import pprint


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
    return droptables

breakers = ['Enemy Name']
mods = []
table = download_tables()
for i in table.select('tr'):
    if i.has_attr('class'):
        continue
    else:
        try:
            if i.th.get_text() in breakers:
                continue
            mods.append(i.th.get_text())
        except:
            continue

pprint.pprint(len(mods))