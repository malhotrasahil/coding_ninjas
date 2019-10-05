import numpy as np
import csv
import time
start=time.process_time()

with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)
    country = list()
    killed = list()
    wounded = list()
    city = list()

    for row in csv_obj:
        if ((row['City'] =='Unknown') or (row['Country'] !='India') ):
            continue
        country.append(row['Country'])
        city.append(row['City'])
        killed.append(row['Killed'])
        wounded.append(row['Wounded'])


country_np=np.array(country)
city_np=np.array(city)
killed_np=np.array(killed)
wounded_np=np.array(wounded)


killed_np[killed_np=='']=0
wounded_np[wounded_np=='']=0
killed_np=np.array(killed_np, dtype=float)
wounded_np=np.array(wounded_np, dtype=float)
casuality=killed_np+wounded_np
casuality_np=np.array(casuality,dtype=int)


# max_array=np.argsort(casuality_np)
# max_array_top5=max_array[-1:-6:-1]

d={}
for i in range(len(city_np)):

        if city_np[i] in d.keys():
            d[city_np[i]]+=casuality_np[i]
        else:
            d[city_np[i]]=casuality_np[i]
x = sorted(d.items(), key = lambda d: (d[1],d[0]))
for i in x[len(x)-1:len(x)-6:-1]:
    print(i[0]," ",int(i[1]))


# for i in max_array_top5:
#     print(city_np[i],' ',casuality_np[i])

print(time.process_time() - start)