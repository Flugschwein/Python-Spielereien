import random
random_items = [random.randint(1, 1000) for c in range(10000)]


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key


print('Before: ', random_items)
insertion_sort(random_items)
print('After : ', random_items)
times = []
length = len(random_items)
for x in range(length):
    times.append(0)
for i in random_items:
    times[i] += 1
    print(i,'->',times[i])
print('Fertig')
count = 0
for y in range(len(times)):
    count += random_items[y]

print(count/len(random_items))
            
