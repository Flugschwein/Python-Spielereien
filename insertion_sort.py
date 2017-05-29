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


print 'Before: ', random_items
insertion_sort(random_items)
print 'After : ', random_items
times = []

for x in range(1,1000):
    times.append(x)
    for i in random_items:
        if i == x:
            times[x] += 1
    print(x, times[x])
print('Fertig')

            
