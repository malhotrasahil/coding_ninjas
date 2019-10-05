# import numpy as np
#
# a=np.arange(1,11)
# b=np.where(a%2!=0)[0]
#
# a[b]=-1
# print(*a)


# _______2ndapproach__________


import numpy as np

a=np.arange(1,11)
a[a%2!=0]=-1

print(*a)