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


def search_mods(mod,tables):
    print(33)


def return_modlist(tables):
    mods = []
    tables = tables.select('#modLocations')[0].next_sibling
    for i in tables.select('tr'):
        if i.has_attr('class'):
            continue
        else:
            try:
                if i.th.get_text() == 'Enemy Name':
                    continue
                mods.append(i.th.get_text().lower())
            except AttributeError:
                continue
    return mods


def return_blueprint_list(tables):
    blueprints = []
    tables = tables.select('#blueprintLocations')[0].next_sibling
    for i in tables.select('tr'):
        if i.has_attr('class'):
            continue
        else:
            try:
                if i.th.get_text() == 'Enemy Name':
                    continue
                blueprints.append(i.th.get_text().lower())
            except AttributeError:
                continue
    return blueprints


def return_relic_list(tables):
    relics = []



def define_input_type(item, tables):
    # 0 = Mod
    # 1 = Blueprint
    # 2 = Blueprint without 'blueprint'
    # 3 = relic
    # 4 = relic without 'relic'
    # 5 = Something else
    mods = return_modlist(tables)
    blueprints = return_blueprint_list(tables)
    relics = return_relic_list(tables)
    item = item.lower()
    if item in mods:
        return 0
    elif item.endswith('blueprint') and item in blueprints:
        return 1
    elif item + ' blueprint' in blueprints:
        return 2
    elif item.endswith('relic') and item in relics:
        return 3
    elif item + ' relic' in relics:
        return 4
    else:
        return


print(return_modlist(download_tables()))
print(len(return_modlist(download_tables())))
print(return_blueprint_list(download_tables()))
print(len(return_blueprint_list(download_tables())))
