from random import randint

roll = randint(1,6)
answer = ''

while answer != 'n':
    print('Du hast',roll, 'gewürfelt!')
    roll = randint(1,6)
    answer = input('Nochmal würfeln?(j/n)')

exit()
