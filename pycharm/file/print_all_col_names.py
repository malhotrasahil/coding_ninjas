import csv

with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    l1=csv.reader(file_obj)
    arr=list()
    # print(type(l1))
    for i in l1:
        arr.append(i)
        break


# del arr[0]
for i in arr[0]:
    print(i)


# year2017.csv