import numpy as np
import csv
import time
start = time.process_time()


with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)
    year=list()
    month=list()
    killed=list()
    wounded=list()
    city=list()
    group=list()

    for row in csv_obj:
        # if ((row['City'] =='Unknown') or (row['Group'] =='Unknown') ):
        #     continue
        # if row['Country']=='India':
        if row['State'] == 'Jammu and Kashmir' and row['Year']=='1999':
            if row['Month']=='5' or row['Month']=='6' or row['Month']=='7':

                # year.append(row['Year'])
                # month.append(row['Month'])
                killed.append(row['Killed'])
                wounded.append((row['Wounded']))
                city.append(row['City'])
                group.append(row['Group'])

# year_np=np.array(year, dtype=int)
# month_np=np.array(month, dtype=int)
killed_np=np.array(killed)
wounded_np=np.array(wounded)
city_np=np.array(city)
group_np=np.array(group)

#for filtering Unknown values from the data
# bool_for_rem_unknown=np.logical_or(city_np=='Unknown',group_np=='Unknown')
# print(bool_for_rem_unknown.size)
#
# year_np=year_np[bool_for_rem_unknown]
# month_np=month_np[bool_for_rem_unknown]
# killed_np=killed_np[bool_for_rem_unknown]
# wounded_np=wounded_np[bool_for_rem_unknown]
# city_np=city_np[bool_for_rem_unknown]
# group_np=group_np[bool_for_rem_unknown]

killed_np[killed_np=='']=0
wounded_np[wounded_np=='']=0
killed_np=np.array(killed_np,dtype=float)
wounded_np=np.array(wounded_np,dtype=float)
casuality_np=killed_np+wounded_np

# bool=np.logical_and(year_np==1999,(np.logical_and(month_np>=5, month_np<=7)))
# print(bool.size)

kargil_arr_cas=casuality_np
# print(kargil_arr_cas.size)
# print(np.max(kargil_arr_cas))
max_index=np.argmax(kargil_arr_cas)
# print(max_index)

kargil_arr_city=city_np
kargil_arr_group=group_np
print(int(kargil_arr_cas[max_index]),' ',kargil_arr_city[max_index],' ',kargil_arr_group[max_index])


print(time.process_time() - start)