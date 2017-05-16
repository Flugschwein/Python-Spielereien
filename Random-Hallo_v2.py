#Import all the needed things.
from random import choice
from time import asctime
from time import sleep

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Create the time the program starts at.
time1 = asctime()

#Generate the first 5 letters.
roll = choice(alphabet)
roll2 = choice(alphabet)
roll3 = choice(alphabet)
roll4 = choice(alphabet)
roll5 = choice(alphabet)
#Set the count to 1.
count = 1
total = (roll + roll2 + roll3 + roll4 + roll5)

#Create a function we are going to need later
def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)

#Print the starting time and the first roll.
print(time1)

print(total)

#Create a loop.
while total != ('hallo'):
    if total != ('hallo') :

#Roll again.
        roll = choice(alphabet)
        roll2 = choice(alphabet)
        roll3 = choice(alphabet)
        roll4 = choice(alphabet)
        roll5 = choice(alphabet)

#Add 1 to the count.
        count += 1
        total = (roll + roll2 + roll3 + roll4 + roll5)

#Print the count and the roll.
        print(count,total)

#Stop the loop if Hallo was generated.
    else:
        break

#Set the time Hallo was created.
time2 = asctime()

#Create a .txt file with the needed rolls in it
save_file(str(count) + '.txt', str([count, time1, time2]))

#Print Hallo, the number of rolls it needed and the time that was needed.
print('Hallo')
print('Es hat ',count,'Versuche gebraucht.')
print('Der Versuch hat von',time1,'bis',time2,'gedauert')

#Ask if the program should close.
frage = input('Willst du das Programm verlassen? (1:Ja/2:Nein)')
while True:

#Close it.
    if frage == '1':
        exit()

#Wait an eternity, then close.
    elif frage == '2':
        sleep(1000000)
        exit()

#Ask again, because the answer was inalid.
    else:
        frage = input('Keine korrekte Eingabe! (1:Ja/2:Nein)')
