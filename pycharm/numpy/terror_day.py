import numpy as np
import csv

with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file_obj:
    csv_obj=csv.DictReader(file_obj)
    # day_list=list()
    # count=0
    # for row in data:
    #     if int(row['Day'])>=10 and int(row['Day'])<=20:
            # day_list.append(row['Day'])
            # count +=1
    # print(count)
    day_list=list()
    for row in csv_obj:
        day_list.append(int(row['Day']))

    np_day=np.array(day_list)

    # print(len(np_day))
    # bool=(np_day[np_day>=10]<=20)
    np_day=np_day[np.logical_and((np_day>=10),(np_day<=20))]


    print(np_day.size)
    # print(bool)

