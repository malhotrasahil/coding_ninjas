# def all_intersection(l1,l2):
#     list_intersection=list()
#     for i in l2:
#         if i in l1:
#             list_intersection.append(i)
#     return list_intersection


# def all_intersection(l1,l2):
#     list_intersection=list()
#     s1=set(l1)
#     s2=set(l2)
#     list_intersection=list(s1&s2)
#     print(list_intersection)
#     list_intersection.sort()
#     return list_intersection
#

def maximum_sum(l1,l2):
    list_intersection=list()
    max_sum=0
    sum1 = 0
    sum2 = 0
    len_l1=len(l1)
    len_l2=len(l2)
    counter=max(len_l1,len_l2)
    i=0
    j=0
    while i <m and j <n:

        if l1[i]<l2[j]:
            sum1 +=l1[i]
            i=i+1
            if i >(len_l1-1):
                max_sum=max_sum + sum(l2[j:])
                break
        else:
            sum2 +=l2[j]
            j=j+1
            if j >(len_l2-1):
                max_sum=max_sum + sum(l1[i:])
                break
        if l1[i]==l2[j]:
            sum1 += l1[i]
            sum2 += l2[j]
            max_sum=max_sum + max(sum1,sum2)
            i = i + 1
            j = j + 1
            sum1,sum2=0,0
            if i >(len_l1-1):
                max_sum=max_sum + sum(l2[j:])
                break
            if j >(len_l2-1):
                max_sum=max_sum + sum(l1[i:])
                break
    return max_sum




m=int(input())
list1=[int(i) for i in input().strip().split(' ')]
n=int(input())
list2=[int(i) for i in input().strip().split(' ')]

# list1=[1,5,10,15,20,25]
# list2=[2,4,5,9,15,17]

# list1=[1,10,20,25]
# list2=[2,4,5,9,15]


max_summ=maximum_sum(list1,list2)
print(max_summ)


