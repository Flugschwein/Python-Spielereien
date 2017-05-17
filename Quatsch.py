import random

def summe(s):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return s[0]
    else:
        mitte = len(s)//2
        s1 = s[:mitte]
        s2 = s[mitte:]
        return summe(s1) + summe(s2)

count = 0
total = 0

for i in range(1,1000000):
    if count%10000 == 0:
        print(count)
    s = [random.randint(1,2) for i in range(1,10)]
    count += 1
    total = total + summe(s)
print(total/count)
