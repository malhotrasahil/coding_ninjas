
import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
# print(csv_obj)
# cnt_ban=0
# cnt_canada=0

dict={}

for row in list1:
    str=row['Posting_date'].split(',')[-1].strip()
    # print(str)
    if str=='2018':
        mon=row['Posting_date'].split(',')[0].strip().split()[0]
        # key=mon
        dict[mon]=dict.get(mon,0) +1

# print(dict)
highest_mon=''
highest_val=0

for k,v in dict.items():
    if v>=highest_val:
        highest_mon=k
        highest_val=v


print (highest_mon,' ',highest_val)
