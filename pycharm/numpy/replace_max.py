import numpy as np


a=np.array([11, 2, 13, 4, 15, 6, 27, 8, 19])

# print(a)
# max=(a.max())

# a[a.max()]=0


# ind=np.where(a==max)

# print(ind)

# a[ind]=0
a[a==a.max()]=0


for i in a:
    print(i)
