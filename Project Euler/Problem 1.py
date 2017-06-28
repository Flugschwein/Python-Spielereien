count3 = 0
count5 = 0
multiples = []
while True:
    temp = (count5+1)*5
    count5 += 1
    if temp < 1000 and temp > 0:
        if temp not in multiples:
            multiples.append(temp)
    else:
        break
while True:
    temp = (count3+1)*3
    count3 += 1
    if temp < 1000 and temp > 0:
        if temp not in multiples:
            multiples.append(temp)
    else:
        break
summe = 0
for i in multiples:
    summe += i
print(summe)