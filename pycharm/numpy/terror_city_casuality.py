import numpy as np
import csv
import time
start=time.process_time()

with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)

    city_cas=list()
    # kill_woun=list()
    for row in csv_obj:
        city_cas.append([row['Country'],row['City'],row['Killed'],row['Wounded']])

# print(len(city_cas))
# print(time.process_time()-start)

city_cas_np=np.array(city_cas)
city_cas_np=city_cas_np[city_cas_np[:,0]=='India']
city_cas_np=city_cas_np[city_cas_np[:,1]!='Unknown']
# print(city_cas_np.size)
# city_cas_np=city_cas_np[city_cas_np[:,1]
# city_cas_np[city_cas_np[:,2] =='']=0.0
# print(sum(city_cas_np[:,2] ==''))
# print(city_cas_np.size)


city_killed_np=np.array(city_cas_np[:,2], dtype=str)
city_wounded_np=np.array(city_cas_np[:,3], dtype=str)
city_killed_np[city_killed_np=='']=0
city_wounded_np[city_wounded_np=='']=0
city_killed_np=np.array(city_killed_np, dtype=float)
city_wounded_np=np.array(city_wounded_np, dtype=float)
casuality_np=city_killed_np+city_wounded_np
casuality_np=np.array(casuality_np,dtype=int)
# print(np.sort(casuality_np))
# print(type(casuality_np))
# print(casuality_np.shape)
# print(city_cas_np.shape)

# city_cas_np=np.append(city_cas_np,casuality_np, axis=1)
city_cas_np=np.insert(city_cas_np, 4, values=casuality_np, axis=1)
# print((city_cas_np.size))

d={}
for i in range(len(city_cas_np)):

        if city_cas_np[i,1] in d.keys():
            d[city_cas_np[i,1]]+=casuality_np[i]
        else:
            d[city_cas_np[i,1]]=casuality_np[i]
x = sorted(d.items(), key = lambda d: (d[1],d[0]))
for i in x[len(x)-1:len(x)-6:-1]:
    print(i[0]," ",int(i[1]))



print(time.process_time() - start)