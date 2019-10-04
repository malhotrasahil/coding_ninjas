def duplicateCount(arr):
    len_arr=len(arr)
    set_arr=set(arr)
    len_set_arr=len(set_arr)
    # print(len_arr)
    # print(len_set_arr)
    return len_arr - len_set_arr

# Main
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(duplicateCount(arr))
