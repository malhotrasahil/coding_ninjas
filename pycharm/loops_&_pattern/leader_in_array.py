n=int(input())
arr=[int(i) for i in input().strip().split(' ')]
#print(arr)

for i in range(n-1):
    arr_last=arr[i+1:]
    # print(arr_last)
    arr_last.sort()
    # print(arr_last)
    largest=arr_last[-1]
    if arr[i]>=largest:
        print(arr[i], end=' ')
print(arr[-1])



#  arr_rev=arr[::-1]
#


# Optimized approach with less complexity of O(n)

n=int(input())
arr=[int(i) for i in input().strip().split(' ')]
#print(arr)

largest=arr[n-1]
leader=[]
leader.append(largest)
for i in range(n-2,-1,-1):
    if arr[i]>=largest:
        leader.append(arr[i])
        largest=arr[i]
m=len(leader)
for i in range(m-1,-1,-1):
    print(leader[i],end=" ")
