n=int(input())
i=1
while i<=n:
    j=1
    space=1
    number=1
    rev_number=i
    count_i=i
    while space<=n-i:
        print(' ',end='')
        space=space+1
    while number<=i:
        print(count_i,end='')
        number = number+ 1
        count_i=count_i +1
    while rev_number>1:
        print(count_i-2,end='')
        rev_number = rev_number - 1
        count_i = count_i - 1

    print()
    i=i+1