def maxDistance(l):
    dict = {}
    for e in l:
        dict[e] = dict.get(e, 0) + 1
    # print (dict)
    duplicate_element_list=list()
    for e in dict:
        if dict[e]>=2:
            duplicate_element_list.append(e)
    # print(duplicate_element_list)
    max_distance=0
    max_distance_element=None
    for e in duplicate_element_list:
        # print(l.index(e))
        # print(rindex(l,e))
        diff=rindex(l,e) - l.index(e)
        if diff > max_distance:
            max_distance=diff
            max_distance_element=e
    return max_distance

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1



# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
# l=[4,1,1,1,2,4,4,4,4,4,4,7,8,9,6,5]
# l=[1,2,3,4,5,6]
print(maxDistance(l))