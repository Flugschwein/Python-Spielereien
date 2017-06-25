from random import choice
name = 'parlich'
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
