n=int(input())

# i=1
# while i<=n:
#     j=1
#     counter=1
#     while j<=n:
#         if j<=n-i:
#             print(' ',end='')
#         else:
#             print(counter,end='')
#             counter+=1
#         j+=1
#     print()
#     i=i+1


i=1
while i<=n:
    j=1
    space=1
    number=1
    while j<=n:
        while space<=n-i:
            print(' ',end='')

        while number<=i:
            print(number,end='')
            j = nnumber+ 1
        j = j + 1
    print()
    i=i+1



