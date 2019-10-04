
import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
print(csv_obj)
print(list1[0])
print()
print(list1[1])
# cnt_ban=0
cnt_canada=0

for row in list1:
    str=row['location'].split(',')[0].strip()
    # print(str)
    if str=='CA':
        cnt_canada +=1


print (cnt_canada)
# IN, KA, Bangalore
# US, WA, Seattle
