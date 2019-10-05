import numpy as np

a=np.array( [[221, 20, 19, 99, 17],  [16 ,5 ,144, 13, 912],  [117 ,4410,  9,  8,  77],  [ 66,  5,  4 , 3 , 200]])
print(a)

col_array=np.argsort(a[:,1])

# print(col_array)
#
print(a[col_array])


# sorted_array=np.sort(a)
#
# print(sorted_array)
