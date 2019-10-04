import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
# print(csv_obj)
# cnt_ban=0
# cnt_canada=0
ba_degree=0

for row in list1:
    str=row['BASIC QUALIFICATIONS']
    # print(str)
    # a=str.find('computer vision')

    if 'Bachelor' in str or 'BA' in str or 'BS' in str:
        ba_degree += 1

    # if a!=-1:
    #     cnt_comp_vision +=1
print (ba_degree)

# print(dict)
