import numpy as np
import csv

with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)
    day=list()
    month = list()
    year = list()
    for row in csv_obj:
        year.append(row['Year'])
        month.append(row['Month'])
        day.append(row['Day'])

year_np=np.array(year,dtype=int)
month_np=np.array(month,dtype=int)
day_np=np.array(day,dtype=int)

bool=np.logical_and(np.logical_and(year_np==2010 , month_np==1),np.logical_and(day_np>=1,day_np<=31))

result=day_np[bool]
print(result.size)