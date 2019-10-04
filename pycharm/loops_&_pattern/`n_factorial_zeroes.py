n=int(input())

count=0
i=5
while i<=n:
    count=count + (n//i)
    i*=5
print(count)