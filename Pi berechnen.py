def calc_pi(length):
    i = 1
    pi = 0
    while True:
        if i%4 == 1:
            pi += (4*(1/i))
        elif i%4 == 3:
            pi -= (4*(1/i))
        if (i-1)/2 >= int(length):
            return pi
        elif (i-1)/2%100000 == 0 and i-1 != 0:
            print('I\'m at '+str(i-1)+' steps.')
        i += 2
print(calc_pi(input('How many operations shall i do?')))
