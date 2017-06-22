pi = '3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446'
pi2 = ''
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
for i in range(101):
    pi2 = pi2 + pi[i]
    print(pi[i])
for i in range(len(pi2)):
    if pi2[i] == '0':
        count0 += 1
    elif pi2[i] == '1':
        count1 += 1
    elif pi2[i] == '2':
        count2 += 1
    elif pi2[i] == '3':
        count3 += 1
    elif pi2[i] == '4':
        count4 += 1
    elif pi2[i] == '5':
        count5 += 1
    elif pi2[i] == '6':
        count6 += 1
    elif pi2[i] == '7':
        count7 += 1
    elif pi2[i] == '8':
        count8 += 1
    elif pi2[i] == '9':
        count9 += 1
    else:
        print('.')
print('0',count0,'\n1',count1,'\n2',count2,'\n3',count3,'\n4',count4,'\n5',count5,'\n6',count6,'\n7',count7,'\n8',count8,'\n9',count9)
