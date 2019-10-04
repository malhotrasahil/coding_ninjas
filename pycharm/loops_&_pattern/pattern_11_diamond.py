import math

n1 = int(input())
n = math.ceil(n1 / 2)
i = 1
while i <= n:
    j = 1
    space = 1
    number = 1
    rev_number = i
    while space <= n - i:
        print(' ', end='')
        space = space + 1
    while number <= i:
        print('*', end='')
        number = number + 1
    while rev_number > 1:
        print('*', end='')
        rev_number = rev_number - 1

    print()
    i = i + 1

n = n1 // 2
i=0
while i<n:
    space=0
    star=1
    rev_star=1
    while space<=i:
        print(' ',end='')
        space +=1
    while star <=n-i:
        print('*', end='')
        star +=1
    while rev_star <=n-i-1:
        print('*', end='')
        rev_star +=1
    i=i+1
    print()