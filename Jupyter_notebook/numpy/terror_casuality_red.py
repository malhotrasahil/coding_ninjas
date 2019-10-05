import numpy as np
import csv

import time
start = time.process_time()
# your code here



with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" ,'r', encoding ='UTF-8') as file:
    csv_obj=csv.DictReader(file, skipinitialspace=True)

    killed=list()
    wounded=list()
    state=list()

    for row in csv_obj:
        if (row['State'] == 'Jharkhand' or row['State'] == 'Odisha' or row['State'] == 'Chhattisgarh' or row['State'] == 'Andhra Pradesh'):

            killed.append(row['Killed'])
            wounded.append((row['Wounded']))
            state.append((row['State']))


    killed_np=np.array(killed)
    wounded_np=np.array(wounded)
    state_np=np.array(state)

#for filtering values of desired states
    # bool_for_states=np.logical_or(np.logical_or(state_np=='Jharkhand',state_np=='Odisha'),np.logical_or(state_np=='Chhattisgarh',state_np=='Andhra Pradesh'))
    #
    # killed_np=killed_np[bool_for_states]
    # wounded_np=wounded_np[bool_for_states]


    killed_np[killed_np=='']=0
    wounded_np[wounded_np=='']=0
    killed_np=np.array(killed_np,dtype=float)
    wounded_np=np.array(wounded_np,dtype=float)

    sum_wou = np.sum(wounded_np)
    sum_kill = np.sum(killed_np)

    sum_cas = sum_wou + sum_kill
    print(int(sum_cas))

print(time.process_time() - start)