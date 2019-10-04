import csv


with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    csv_obj=csv.DictReader(file_obj,skipinitialspace=True)
    print(type(csv_obj))
    list1=list(csv_obj)


print(list1[1])
no_casuality=0
for row in list1:
    if row['Weapon_type'].lower()=='explosives':
        if row['casualities']!='':
            no_casuality += float(row['casualities'])
print(int(no_casuality))



