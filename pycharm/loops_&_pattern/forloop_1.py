
######################   1st way ##########################
# n=int(input())
#
#
#
# list1=[]
# x=1
# while len(list1)<n:
#     y=3*x+2
#     if y%4 !=0:
#         list1.append(y)
#     x=x+1
#
# for c in list1:
#     print(c,end=' ')
#
#####################################################
############ 2nd way  ################

n=int(input())
i=1
while n>0:
    x = 3 * i + 2
    if x%4 !=0:
        print(x , end=' ')
        i=i+1
    else:
            i=i+1
            n=n+1
    n=n-1


##############################################

########### 3rd Way ############################

n=int(input())
i=1
while n>0:
    x = 3 * i + 2
    if x%4 !=0:
        print(x , end=' ')
        i=i+1
    else:
            i=i+1
            n=n+1
    n=n-1

###################################################





# for i in range(1,p):
#     x=3*i+2
#     if x%4 !=0:
#         print(x , end=' ')
#     else:
#         p=p+1
# print()
# print(p)
#





# for i in range(1,11):
#     x=3*i+2
#     if x%4 !=0:
#         print(x , end=' ')
#

# p=11