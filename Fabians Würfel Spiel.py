#! /usr/bin/python
from random import randint
noholes = {1:0,2:0,3:0,4:0,5:0}
count = 0
individualcount = 0
maxcount = 0
mincount = 0
times = input('How many games should be simulated?')
player_count = input('How many Players should participate in the game?')
players = {}
wins = {}
for p in range(int(player_count)):
    wins[p + 1] = 0
for i in range(int(times)):
    for p in range(int(player_count)):
        players[p+1] = 36 // int(player_count)
    noholes = {1:0,2:0,3:0,4:0,5:0}
    individualcount = 0
    while min(players.values()) > 0:
        for x in players:
            roll = randint(1,6)
            individualcount += 1
            if roll < 6:
                if noholes[roll] is 0:
                    noholes[roll] += 1
                    players[x] -= 1
                    if players[x] is 0:
                        wins[x] += 1
                        break
                    elif noholes[roll] is 1:
                        noholes[roll] -= 1
                        players[x] += 1
            elif roll is 6:
                players[x] -= 1
                if players[x] is 0:
                    wins[x] +=1
                    break
    count += individualcount
    if i is 0:
        high = individualcount
        low = individualcount
    elif i > 0:
        if individualcount > high:
            high = individualcount
            maxcount = 1
        elif individualcount < low:
            low = individualcount
            mincount = 1
        elif individualcount == low:
            mincount += 1
        elif individualcount == high:
            maxcount += 1
    if (i+1) % 1000 == 0:
        print(str(i+1) + '\t|' + str(count/(i+1)))
print('Der Durchschnitt an benoetigten Wuerfeln um das Spiel zu beenden von '+str(times)+' simulierten Spielen liegt bei: '+str(int(count)/int(times)))
print('Fuer das laengste Spiel ('\
      + str(maxcount)+\
      ' mal) musste '\
      + str(high)\
      + ' mal gewuerfelt werden.')
print('Fuer das kuerzeste Spiel ('\
      + str(mincount)\
      + ' mal) musste '\
      + str(low)\
      + ' mal gewuerfelt werden.')
for i in wins:
    print('Spieler '\
          + str(i)\
          + ' hat '\
          + str(wins[i])\
          + ' mal gewonnen')