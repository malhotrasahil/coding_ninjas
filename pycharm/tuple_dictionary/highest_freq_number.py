def maxFreq(l):
    dict={}
    for e in l:
        dict[e]=dict.get(e,0) +1
    # print (dict)
    a=max(dict.values())
    # print(a)

    max_occur=None
    for e in l:
        if dict[e]>dict.get(max_occur,0):
            max_occur=e
    freq=dict[max_occur]



    return max_occur




# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
# l=[4,1,1,1,1,1,1,1,2,4,4,4,4,4,4,7,8,9,6,5]
print(maxFreq(l))



# ^^^^^^^^^^^^^^^^^^^^^^second method^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def maxFreq(l):
    dict={}
    for e in l:
        dict[e]=dict.get(e,0) +1
    # print (dict)
    a=max(dict.values())
    # print(a)
    list_common_freq=list()
    for k,v in dict.items():
        if v==a:
            list_common_freq.append(k)
    print (list_common_freq)
    first_occur=None
    for i in l:
        if i in list_common_freq:
            first_occur=i
            break
    print("the first occur is ",first_occur )
    max_occur=None
    for e in l:
        if dict[e]>dict.get(max_occur,0):
            max_occur=e
    freq=dict[max_occur]



    return max_occur




# Main
# n=int(input())
# l=list(int(i) for i in input().strip().split(' '))
l=[5,6,5,4,1,1,1,1,1,1,1,2,4,4,4,4,4,4,7,8,9,6,5]
print(maxFreq(l))
