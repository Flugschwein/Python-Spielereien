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
count = 0
total = (roll + roll2 + roll3 + roll4 + roll5)

#Create two functions we are going to need later
def save_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
def open_file(filename):
    f = open(filename, 'r')
    read = f.read().splitlines()
    return read
def Summe(liste):
    Zwischensumme = 0
    for i in range(len(liste)):
        Zwischensumme += int(liste[i])
    return Zwischensumme

#Print the starting time and the first roll.
print(time1)

print(count)

#Create a loop.
while total != ('hallo'):
    
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
    if count%100000 == 0:
        print(count)
#Set the time Hallo was created.
time2 = asctime()

#Create a .txt file with the needed rolls in it
save_file('Results/txt' + str(count) + '.txt', str([count, time1, time2]))
R = open('Results/Results.csv', 'a')
R.write(str(int(count))+'\n')
R.close()
Results = open_file('Results/Results.csv')
print('Results: ',Results)
text = str('Anzahl,Summe,Durchschnitt\n'+str(len(Results))+','+str(Summe(Results))+','+str(Summe(Results)/len(Results)))
save_file('Results/Statistik.csv',text)

#Print Hallo, the number of rolls it needed and the time that was needed.
print(total)
print('Es hat ',count,'Versuche gebraucht.')
print('Der Versuch hat von',time1,'bis',time2,'gedauert')

#Ask if the program should close.
frage = input('Willst du das Programm verlassen? 1=Ja\n')
while True:

#Close it.
    if frage == '1':
        exit()
#Ask again, because the answer was inalid.
    else:
        frage = input('Keine korrekte Eingabe! (1=Ja)\n')
