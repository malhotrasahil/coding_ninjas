str=input()


l=str.split(' ')

# for i in l:
#     for j in range(len(i)-1,-1,-1):
#          print(i[j], end='')
    # print(' ', end='')



for i in l:
    print(i[::-1], end=' ')


