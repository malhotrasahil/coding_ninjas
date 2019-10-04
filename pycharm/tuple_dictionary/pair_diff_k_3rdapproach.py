def printPairDiffK(l, k):
    arr=list()
    l_bkp=list(l)
    counter=len(l)
    dict={}
    for i in l:
        dict[i]=dict.get(i,0) +1

    for key,val in dict.items():
        expected_val_1=k+key
        expected_val_2=key-k
        if expected_val_1 in l:




    return arr





n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
arr=printPairDiffK(l, k)

for i in arr:
    print(*i)