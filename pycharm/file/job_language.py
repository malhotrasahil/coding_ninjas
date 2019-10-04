import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)

ba_degree=0

dict={}

for row in list1:
    str=row['BASIC QUALIFICATIONS']
    if 'Bachelor' in str or 'BA' in str or 'BS' in str:
        country = row['location'].split(',')[0].strip()
        # print(str)
        if country == 'IN':
            if 'Java' in str:
                dict['Java']=dict.get('Java',0) +1
            if 'C++' in str:
                dict['C++'] = dict.get('C++', 0) + 1
            if 'Python' in str:
                dict['Python'] = dict.get('Python', 0) + 1

language=''
max_count_lan=0
for k,v in dict.items():
    if v>=max_count_lan:
        max_count_lan=v
        language=k

print(language,' ',max_count_lan)

# print(dict)
