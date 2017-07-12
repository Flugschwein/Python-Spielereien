eng = open('Skilllist JP.csv','r',encoding='UTF-8')
alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-+, '
result = ''
r = eng.read()
r = r.splitlines()
for i in r:
    if i[1] in alphabet:
        pass
    else:
        for b in i:
            result += b
        result += '\n"'
neweng = open('NewSkilllist JP.csv', 'w',encoding='UTF-8')
neweng.write(result)
print(result)