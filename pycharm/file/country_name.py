import csv


with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    csv_obj=csv.reader(file_obj)
    l1=list(csv_obj)

for i in range(1,11):
    print(l1[i][3])




