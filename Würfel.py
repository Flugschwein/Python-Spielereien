from random import randint

roll = randint(1,6)
second_roll = randint(1,6)

if roll < 6 :
    print('Du hast',roll, 'gewürfelt!')

else :
    print('Du hast 6 gewürfelt!')
    print('Weil du eine 6 gewürfelt hast, darfst du noch einmal würfeln!')
    print('Dein zusätzlicher Wurf ist eine',second_roll,'!')



