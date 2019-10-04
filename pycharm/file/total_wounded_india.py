import csv
with open("C:\\Users\\Sahil\\Downloads\\year2017.csv") as file_obj:
    csv_obj=csv.reader(file_obj,skipinitialspace=True)
    l=list(csv_obj)
# arr=list()
# print(l[:5])
# wounded_sum=0
# for l1 in l[1:]:
#     if l1[10]=='':
#         continue
#     wounded_sum=wounded_sum+ (int(l1[10]))

arr=list()
for l1 in l[1:]:
    if l1[10] == '':
        continue
    elif l1[3].lower()=="india":
        
        arr.append(float(l1[10]))

print(int(sum(arr)))



# print(wounded_sum)

