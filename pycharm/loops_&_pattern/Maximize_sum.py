def all_intersection(l1,l2):
    return list(set(l1).intersection(set(l2)))


m=int(input())
list1=[int(i) for i in input().strip().split(' ')]
n=int(input())
list2=[int(i) for i in input().strip().split(' ')]

# list1=[1,5,10,15,20,25]
# list2=[2,4,5,9,15]

# list1=[1,10,20,25]
# list2=[2,4,5,9,15]


intersected_elements=all_intersection(list1,list2)
intersected_elements.sort()
# print(intersected_elements)

if intersected_elements==[]:
    sum_l1=sum(list1)
    sum_l2=sum(list2)
    if sum_l1>=sum_l2:
        print(sum_l1)
    else:
        print(sum_l2)
else:
    summ=0
    l1_intersected_index=[ list1.index(i) for i in intersected_elements]
    l2_intersected_index=[ list2.index(i) for i in intersected_elements]
    len_intersected_elements=len(intersected_elements)
    for i in range(len_intersected_elements+1):
        if i==0:
            # a=l1_intersected_index[i]
            # blist=list()
            # blist=list1[i:a]
            sum_l1 = sum(list1[i:l1_intersected_index[i]])
            # print(blist)
            # print(type(blist))
            # sum_l19 = sum([1])
            # print(sum_l1)
            sum_l2 = sum(list2[i:l2_intersected_index[i]])
            if sum_l1>=sum_l2:
                summ += sum_l1
            else:
                summ += sum_l2
        elif i==len_intersected_elements:
            sum_l1 = sum(list1[l1_intersected_index[i-1]:])
            sum_l2 = sum(list2[l2_intersected_index[i-1]:])
            if sum_l1 >= sum_l2:
                summ += sum_l1
            else:
                summ += sum_l2
        else:
            sum_l1 = sum(list1[l1_intersected_index[i-1]:l1_intersected_index[i]])
            sum_l2 = sum(list2[l2_intersected_index[i-1]:l2_intersected_index[i]])
            if sum_l1 >= sum_l2:
                summ += sum_l1
            else:
                summ += sum_l2

    print(summ)







