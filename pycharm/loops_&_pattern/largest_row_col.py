def largestRowCol(arr):
    # Please add your code here
    sum_arr_row = []
    for i in range(m):
        sum=0
        for j in range(n):
            sum=sum +arr[i][j]
        sum_arr_row.append(sum)
    # print("row",sum_arr_row)
    row_max=max(sum_arr_row)
    # print(row_max)

    sum_arr_col = []
    for j in range(n):
        sum=0
        for i in range(m):
            sum=sum +arr[i][j]
        sum_arr_col.append(sum)
    # print("col", sum_arr_col)
    col_max = max(sum_arr_col)
    # print(col_max)

    if row_max>=col_max:
       ret_list=['row' ,sum_arr_row.index(row_max),row_max]
       return ret_list
    else:
       ret_list = ['column', sum_arr_col.index(col_max), col_max]
       return ret_list


#Main
m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
l=largestRowCol(arr)
print(*l)
