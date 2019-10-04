def evenCount(l):
    dict = {}
    for e in l:
        dict[e] = dict.get(e, 0) + 1
    # print (dict)
    for e in l:
        if dict[e]%2==0:
            return e
    else:
        return -1



# Main
# n=int(input())
# arr=list(int(i) for i in input().strip().split(' '))
arr=[2,5,3,5,3,4]
print(evenCount(arr))
