def sum1(ar,start,end):
    ar_split=ar[start:end+1]
    return sum(ar_split)

def equilibriumIndex(arr):
    a=arr[0]
    b=sum(arr[2:])
    for i in range(1,n-1,1):
        # first=sum1(arr,0,i-1)
        # second=sum1(arr,start=i+1,end=n-1)
        first =a
        second=b
        if first==second:
            return i
        a=a+arr[i]
        b=b-arr[i+1]
    else:
        return -1

# Main
n = int(input())
arr = [int(i) for i in input().strip().split()]
print(equilibriumIndex(arr))
