from urllib.request import urlopen
import time
import bs4
import shelve


def download_tables():
    print('Downloading droptables...')
    droptables = urlopen('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    print('Processing droptables...')
    droptables = bs4.BeautifulSoup(droptables, 'html.parser')
    return droptables.prettify()


def loop():
    cur = ''
    prev = download_tables()
    i = 0
    start = time.time()
    print(start)
    while True:
        cur = download_tables()
        if cur == prev:
            print('Nothing changed.\nWaiting 5 minutes. Then trying again.')
            time.sleep(300)
            prev = cur
            continue
        else:
            print('Found a change!!')
            changetime = time.time()
            i += 1
            with open('old-droptables%s.html' %(i), 'w') as old, open('new-droptables%s.html' %(i), 'w') as new, shelve.open('times') as shelf:
                shelf['start'] = start
                shelf['change' + str(i)] = changetime
                old.write(prev)
                new.write(cur)
                old.close()
                new.close()
                shelf.close()
            prev = cur
            continue
loop()
    
