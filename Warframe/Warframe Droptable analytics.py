#! /usr/bin/env python3
import bs4
from urllib.request import urlopen


def download_tables():
    print('Downloading droptables...')
    droptables = ''
    try:
        droptables = urlopen('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    except:
        print('Downloading failed!\nCheck your internet connection and try again.')
        exit()
    print('Processing droptables...')
    droptables = bs4.BeautifulSoup(droptables)
    return droptables


def search_mods(mod, tables):
    headers = tables.select('#modLocations')[0].next_sibling.select('th')
    i = 0
    while headers[i].get_text().lower() != mod:
        i += 1
    mod_header = headers[i]
    cur_mod_drop = mod_header.parent.next_sibling.next_sibling
    drops = {}
    while not cur_mod_drop.has_attr('class'):
        enemy, mod_drop_chance, chance = cur_mod_drop.children
        drops[enemy] = (mod_drop_chance, chance)
        cur_mod_drop = cur_mod_drop.next_sibling
    for i in drops:
        print(i.get_text()+'\t'+drops[i][0].get_text()+'\t'+drops[i][1].get_text())


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
    tables = tables.select('#relicRewards')[0].next_sibling
    for i in tables.select('tr'):
        if i.has_attr('class'):
            continue
        else:
            try:
                i = i.th.get_text().lower()
                if i.endswith(' (intact)'):
                    i = i[:-9]
                if i.endswith(' (exceptional)'):
                    i = i[:-14]
                if i.endswith(' (flawless)'):
                    i = i[:-11]
                if i.endswith(' (radiant)'):
                    i = i[:-10]
                relics.append(i)
                continue
            except AttributeError:
                continue
    return set(relics)


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
        return 5

tables = download_tables()
testItems = ['Corrosive Projection', 'axi a2', 'wAR BlueprinT', 'dread', 'paris prime blueprint', 'Lith n3 Relic', 'vItAl SeNsE', 'Serration']
for i in testItems:
    print(i)
    print(define_input_type(i, tables))
    if define_input_type(i, tables) == 0:
        search_mods(i.lower(), tables)
