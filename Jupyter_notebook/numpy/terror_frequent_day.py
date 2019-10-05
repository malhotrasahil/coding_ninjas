import numpy as np
import csv
import time
start = time.process_time()


with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)

    day=list()


    for row in csv_obj:
        if ((row['Day'] =='0')):
            continue
        day.append(row['Day'])


# year_np=np.array(year, dtype=int)
# month_np=np.array(month, dtype=int)
day_np=np.array(day)
# print(day_np.size)

#for filtering Unknown values from the data
# bool_for_rem_unknown=np.logical_or(city_np=='Unknown',group_np=='Unknown')
# print(bool_for_rem_unknown.size)

val,freq = np.unique(day_np,return_counts = True)
print(val)
print(freq)
maxi=np.max(freq)

max_freq=np.argsort(freq)
max_freq_index=max_freq[-1]
print(max_freq_index)
print(val[max_freq_index],' ',maxi)




# print(time.process_time() - start)