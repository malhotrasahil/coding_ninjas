n=int(input())

i=1
while i<=n:
    j=1
    while j<=n:
        if j<=n-i:
            print(' ',end='')
        else:
            print('*',end='')
        j+=1
    print()
    i=i+1

