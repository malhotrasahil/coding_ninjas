def rowWiseSum(arr):
    output=list()
    for i in arr:
        output.append(sum(i))
    return output


#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
# l=[int(i) for i in input().strip().split(' ')]
#arr1 = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]

arr=[ [ l[i*n +j ]for j in range(n)] for i in range(m)]
print(arr)
l=rowWiseSum(arr)
print(*l)
# for k in l:
#     print(k, end=' ')

##&&&&lengthy way   &&&&#######
# print(m,n)
# arr=list()
#
# element=0
# for i in range(0,m):
#     row_temp = list()
#     for j in range(0,n):
#         row_temp.append(l[element])
#         element +=1
#     arr.append(row_temp)

# print(arr)

