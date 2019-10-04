import numpy as np


a=np.array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])

# print(a)


arr=np.where(a%3==0)
b=arr[0]
print(*b)
