from random import choice
name = 'parlich zunachst schonste ihr abraumen mehrmals der. Gang meer noch mi gern tust ja. Ei du sorglich ku feinheit behutsam. Achtzehn trillern den heiraten oha tadellos man. Hochmut so du gebogen an ja gerufen. Umwolkt barbara bereits du ahnlich da langsam mi schurze. Ans name tust mut lang etwa. Feierabend fluchtigen er leuchtturm nachmittag um hereintrat mi marktplatz. Einfand zweimal kindern wachter jungfer zu zuhorte es. Gestorben la vermodert leuchtete schwemmen schnupfen la plaudernd. Also zu sage so ding. Ihm nah ordnung gewogen fenster oha stopfen bosheit mir dunklen. Ein die erstaunen verharrte rausperte nun stuckchen. Zu du schon zwirn trost. Harmlos fremder man dunklen mir neu all. Stadt er davon klare naher ahren im. Blies takte uhr bibel winde all stuck wette nie wie. Licht se dahin indem seine ku zu karte. Kurios bin minder kam diesen stille den schien. Lief laut so du meer da. Ku er wu offnung gesicht wachsam du zuhorer. Geschwatzt am arbeitsame ei vormittags hufschmied mi jahreszeit auskleiden. Leber ein funfe dem gutes. Brauchen bummelte in kurioses gepflegt launigen zu. Ja so aufgespart um ja fluchtigen betrachtet lattenzaun. Nachmittag vorpfeifen federdecke sah getunchten befangenen was vom zog. Vor viere nie hab leben gehts. Dahinging duftenden hei wir einfacher. Uhr ware mirs kerl nest denn nie. Darauf vielem zu freute ja lehren eifrig pfeife am la. Einen glitt sa gutes blieb pa in leuen. Drunten als fingern nur glatter abwarts alt ist. Wei sammelt niedere glatten und beschlo. Du te schuftet unbeirrt gewartet kollegen in zugvogel mehrmals. La brannten aufstand zu verwohnt gegessen gemessen lauschte. Und fast seid sage sei geht ding. Hatt haus ziel zur teil jede orte hof. Bei scherzwort wasserkrug ehe launischen. Ich recht dus alter reden mit muhle sagst gro. Auch er denn aber la. Duftenden ri in sorglosen nachgehen. Bette la alles um wenns bibel angst. Seiner kostet himmel lie fehlen gut blo ist. Dienstmagd grundstuck zueinander schuchtern gutmutigen vielleicht es in zu. Uber halb sehe ku mirs so ganz dort ri. '
alphabet = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ .!?'
count = 0
total = ''
letter = ''
for i in name:
    while letter is not i:
        letter = choice(alphabet)
        count += 1
        print(count, total)
    total = total + letter
print(count,total)
print(len(name))
