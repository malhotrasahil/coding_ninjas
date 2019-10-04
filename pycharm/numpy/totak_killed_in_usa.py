import numpy as np
import csv
with open("C:\\Users\\Sahil\\Downloads\\terrorismData.csv" , encoding ='UTF-8') as file_obj:
    # csv_obj=csv.reader(file_obj)
    csv_obj = csv.DictReader(file_obj,skipinitialspace=True)
    # list1=list(csv_obj)

    killed=list()
    for row in csv_obj:
        if row['Country']=='United States':
            killed.append(row['Killed'])

    np_killed=np.array(killed)
    np_killed[np_killed=='']='0.0'
    np_killed=np.array(np_killed , dtype=float)
    print(int(np.sum(np_killed)))







