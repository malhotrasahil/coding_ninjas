import numpy as np

arr=np.array([1,2,0,0,4,0])

# print(arr)


indx=np.where(arr!=0)

# print(indx)
# print(type(indx))

i=indx[0]
print(*i)