# m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
# row
m=l[0]
#column
n=l[1]
arr=l[2:]

# arr_matrix=[ [ arr[i*n +j ]for j in range(n)] for i in range(m)]
arr_matrix=[arr[i*n:(i+1)*n] for i in range(m)]

#print(arr_matrix)
for j in range(n):
    if j%2==0:
        for i in range(m):
            print(arr_matrix[i][j],  end=' ')
    else:
        for i in range(m-1,-1,-1):
            print(arr_matrix[i][j], end=' ')

#3 4 1 2 3 4 5 6 7 8 9 10 11 12




