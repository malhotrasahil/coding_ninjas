
import csv

with open("C:\\Users\\Sahil\\Downloads\\amazon_jobs_dataset.csv", encoding ='UTF-8') as file_obj:
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
# print(csv_obj)

cnt_comp_vision=0

for row in list1:
    str=row['Title'].lower()
    # print(str)
    # a=str.find('computer vision')

    if 'computer vision' in str:
        cnt_comp_vision += 1

    # if a!=-1:
    #     cnt_comp_vision +=1



print (cnt_comp_vision)

