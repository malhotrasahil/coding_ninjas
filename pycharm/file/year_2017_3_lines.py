import csv

with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    l1=csv.reader(file_obj)
    arr=list()
    # print(type(l1))
    # print(l1[0])
    l2=list(l1)
    print(l2[0:2])

    for j in range(4):
        for i in l1:
            arr.append(i)
            break


del arr[0]
for i in arr:
    print(*i)

# year2017.csv