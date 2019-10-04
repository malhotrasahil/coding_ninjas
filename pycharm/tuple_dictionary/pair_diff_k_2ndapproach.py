def printPairDiffK(l, k):
    arr=list()
    l_bkp=list(l)
    counter=len(l)
    for j in range(1,counter-1):
        if l[0] -l[j]==k or l[j] -l[0]==k :
            if l[j] > l[0]:
                list1 = list([l[0], l[j]])
            else:
                list1 = list([l[j], l[0]])
            arr.append(list1)
            del l[0]
        print(arr)
        counter = counter -1

    return arr





n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
arr=printPairDiffK(l, k)

for i in arr:
    print(*i)