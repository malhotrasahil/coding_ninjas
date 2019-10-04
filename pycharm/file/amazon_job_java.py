import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)



dict={}

for row in list1:
    str=row['BASIC QUALIFICATIONS']
    if 'Java' in str:
        country = row['location'].split(',')[0].strip()
        dict[country]=dict.get(country,0) +1


country=''
max_count=0
for k,v in dict.items():
    if v>=max_count:
        max_count=v
        country=k

print(country,' ',max_count)

# print(dict)
