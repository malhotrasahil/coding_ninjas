def spiralPrint(arr):

    while arr:
        for i in arr:
            print(*i , end =' ')
            arr.pop(0)
            break
        if arr:
            for i in range(len(arr)):
                if arr[i]==[]:
                    arr.pop(i)
                    break
                print(arr[i][-1] , end =' ')
                arr[i].pop(-1)

        if arr:
            arr_last_rev=arr[-1][::-1]
            for i in arr[-1]:
                arr.pop(-1)
                print(*arr_last_rev , end =' ')
                break

        if arr:
            for i in range(len(arr)-1,-1,-1):
                if arr[i]==[]:
                    arr.pop(i)
                    break
                print(arr[i][0] , end=' ')
                arr[i].pop(0)


# Main
l=[int(i) for i in input().strip().split(' ')]
m, n=l[0], l[1]
arr = [ [ l[(j*n)+i+2] for i in range(n)] for j in range(m)]
# print(arr)
spiralPrint(arr)



# 6 3 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18