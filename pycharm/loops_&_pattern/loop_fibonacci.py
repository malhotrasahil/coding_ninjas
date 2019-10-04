n=int(input())

# f0=1
# f1=1
# def fib(a):
#     if a==0 :
#         return 0
#     elif a==1:
#         return 1
#     return (fib(a-1) + fib(a-2))
#
# sum=0
# if n >=3:


#     for i in range (3,n+1,3):
#         sum = sum + fib(i)
#     print(sum)
# else:
#     print(sum)
#

# 0,1,1,2,3,5,8,13,21,34,55,89,144

sum=0
# sum1=0
b=1
c=1
a = b + c
i=-1


if n >=2:
    # for i in range (3,n+1,3):
    while a<=n:
        a = b + c
        i = i + 1
        if i%3==0:
            sum = sum + a
        if sum>n:
            sum=sum -a
        #     break
        b,c=a,b

        # tmp=b
        # b=a
        # c=tmp

    print(sum)
else:
    print(sum)



#######################

n=int(input())

