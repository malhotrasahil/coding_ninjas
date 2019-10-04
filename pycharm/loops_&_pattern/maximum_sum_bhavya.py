input()
l1 = [int(i) for i in input().split()]
input()
l2 = [int(i) for i in input().split()]

common = set(l1).intersection(set(l2))
com = list(common)
com.sort()

sum_a = 0
if len(com) == 0:
    if sum(l1) > sum(l2):
        sum_a = sum(l1)
    else:
        sum_a = sum(l2)
else:
    i1 = 0
    i2 = 0

    for i in com:
        s1 = 0
        s2 = 0
        for j in range(i1, len(l1)):
            s1 = s1 + l1[j]
            if l1[j] == i:
                break
        for k in range(i2, len(l2)):
            s2 = s2 + l2[k]
            if l2[k] == i:
                break
        if s1 > s2:
            sum_a = sum_a + s1
            # flag = 'l1'
        else:
            sum_a = sum_a + s2
            # flag = 'l2'
        i1 = j + 1
        i2 = k + 1

    else:
        s1 = 0
        s2 = 0
        for i in range(i1, len(l1)):
            s1 = s1 + l1[i]
        for j in range(i2, len(l2)):
            s2 = s2 + l2[j]
        if s1 > s2:
            sum_a = sum_a + s1
        else:
            sum_a = sum_a + s2

print(sum_a)