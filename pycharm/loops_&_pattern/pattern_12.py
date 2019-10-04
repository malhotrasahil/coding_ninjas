n=int(input())

i=0
while i<=n:
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






 # ***
 #  **
 #   *