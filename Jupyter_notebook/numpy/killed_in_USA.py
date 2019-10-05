import numpy as np
import csv
with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" , encoding ='UTF-8') as file_obj:
    # csv_obj=csv.reader(file_obj)
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    list1=list(csv_obj)
    # list2=list1[0:][3]
    # print(list2)
# arr=np.array(list2)


# for row in list1:
#     if row['Country']=='United States':
#         if row['Killed'] !='':
#             print(int(float(row['Killed'])))
#         else:
#             print(0)
#
country=list()
killed=list()
for row in list1:
    killed.append(row['Killed'])
    country.append(row['Country'])

# print(country)

np_country=np.array(country)
np_killed=np.array(killed)
np_killed[np_killed=='']='0.0'
np_killed=np.array(np_killed , dtype=float)
country_us_bool=(np_country=='United States')
# print(country_us_bool)
killed_us=np_killed[country_us_bool]

# killed_us=np.array(killed_us , dtype=int)

for i in killed_us:
    print(int(i))





