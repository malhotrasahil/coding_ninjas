import csv


with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    csv_obj=csv.DictReader(file_obj, skipinitialspace=True)
    list1=list(csv_obj)


# print(list1[1])
dict={}
for row in list1:
    key=row['Month']

    value= row['Killed']

    if key==('' or ' '):
        continue
    if value !='':
        value = int(float(row['Killed']))
    else:
        value=0

    dict[key] = dict.get(key,0) + value

# print(dict)
for k,v in dict.items():
    print(k ,' ', v)
