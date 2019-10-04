def differentNames(l):
    dict={}
    for e in l:
        dict[e] = dict.get(e, 0) + 1
    # print (dict)
    dict_new={}
    for e in dict:
        if dict[e]!=1:
            dict_new[e]=dict[e]

    return dict_new






# Main
# names=input().strip().split()
names=['sahil', 'kunal', 'kunal', 'manu','manu', 'kk']
m=differentNames(names)
if m:
    for name in m:
        print(name, m[name])
else:
    print(-1)
