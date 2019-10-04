a=int(input("enter the number"))
b=int(input("enter the operation"))


if b==1:
    result=0
    for i in range(1,a+1):
        result=result+i



elif b==2:
    result=1
    for i in range(1,a+1):
        result=result*i


else:
    result = -1

print(result)