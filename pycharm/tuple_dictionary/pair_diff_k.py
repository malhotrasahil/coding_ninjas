def printPairDiffK(l, k):
    arr=list()

    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if (l[j]-l[i]==k) or (l[i]-l[j]==k):
                if l[j]>l[i]:
                    list1=list([l[i],l[j]])
                else:
                    list1=list([l[j],l[i]])
                arr.append(list1)
    # for i in range(len(arr)):
    #     arr[i].sort()
    return arr

    # print(arr)





n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
arr=printPairDiffK(l, k)

for i in arr:
    print(*i)