#! /usr/bin/python
from random import randint
players = {1:9,2:9,3:9,4:9}
nohole = [1,2,3,4,5]
noholes = {1:0,2:0,3:0,4:0,5:0}
count = 0
individualcount = 0
times = input('How many games should be simulated?')
for i in range(times):
    players = {1:9,2:9,3:9,4:9}
    noholes = {1:0,2:0,3:0,4:0,5:0}
    individualcount = 0
    while players[1] is not 0 and players[2] is not 0 and players[3] is not 0 and players[4] is not 0:
        for x in players:
            roll = randint(1,6)
            count += 1
            individualcount += 1
            if roll in nohole:
                if noholes[roll] is 0:
                    noholes[roll] += 1
                    players[x] -= 1
                    if players[x] is 0:
                        break
                    elif noholes[roll] is 1:
                        noholes[roll] -= 1
                        players[x] += 1
            elif roll is 6:
                players[x] -= 1
                if players[x] is 0:
                    break
    print(str(i)+'\t|'+str(individualcount))
print('Der Durchschnitt an benoetigten Wuerfeln um das Spiel zu beenden von '+str(times)+' simulierten spielen liegt bei:'+str(count/times))
#told you
