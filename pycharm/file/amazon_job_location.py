
import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
# print(csv_obj)
cnt_ban=0
cnt_us=0

for row in list1:
    str=row['location'].split(',')[-1].strip()
    # print(str)
    if str=='Bangalore':
        cnt_ban +=1
    elif str=='Seattle':
        cnt_us +=1


print (cnt_ban,' ', cnt_us)
# IN, KA, Bangalore
# US, WA, Seattle
