n=int(input())
arr=[i for i in input().split()]

#print(arr)


for i in range(0,n-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]

for i in arr:
    print(i, end=' ')