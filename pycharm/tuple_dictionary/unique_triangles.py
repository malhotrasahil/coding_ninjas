def unique_tri(arr):
    for i in arr:
        i.sort()
    print(arr)
    tuple1=None
    arr1=list()
    for i in arr:
        # del arr[i]
        arr1.append(tuple(i))
    print(arr1)
    dict = {}
    for e in arr1:
        dict[e] = dict.get(e, 0) + 1
    print (dict)
    ret_arr=list()
    for e in dict:
        if dict[e]==1:
            ret_arr.append(e)
    return len(ret_arr)





#main
# n=int(input())
arr=list()
# for j in range(n):
#     arr.append(list(int(i) for i in input().strip().split(' ')))
arr=[[1, 2, 3], [3, 2, 1], [4, 6, 5],[2,3,1],[4, 6, 5]]
# print(arr)
print(unique_tri(arr))

# 3
# 1 2 3
# 3 2 1
# 4 6 5
