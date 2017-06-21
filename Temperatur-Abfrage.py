#!/usr/bin/python
# coding=utf-8


import os, sys, time


def aktuelleTemperatur():
      
    # 1-wire Slave Datei lesen
    file = open('/sys/bus/w1/devices/28-0416c1c236ff/w1_slave')
    filecontent = file.read()
    file.close()

    # Temperaturwerte auslesen und konvertieren
    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    temperature = float(stringvalue[2:]) / 1000

    # Temperatur ausgeben
    rueckgabewert = '%6.2f' % temperature 
    return(rueckgabewert)

schleifenZaehler = 0
schleifenAnzahl = 20
schleifenPause = 120


print("Temperaturabfrage für ", schleifenAnzahl, " Messungen alle ", schleifenPause ," Sekunden gestartet")

while schleifenZaehler <= schleifenAnzahl:
    messdaten = aktuelleTemperatur()
    print("Aktuelle Temperatur : ", messdaten, "°C", "in der ", schleifenZaehler, ". Messabfrage")
    time.sleep(schleifenPause)
    schleifenZaehler = schleifenZaehler + 1
    

print ("Temperaturabfrage beendet")
