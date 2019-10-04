n=int(input())

arr=[]
arr_even=[]
for i in range(1,n+1):
    if (i%2)!=0:
        arr.append(i)
    else:
        arr_even.insert(0,i)

print(*arr+arr_even)
# print(arr_even)


