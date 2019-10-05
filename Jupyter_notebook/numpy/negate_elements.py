import numpy as np
a=np.arange(1,11)
# print(a)

a[(a>=3)&(a<=8)] *=-1

for i in a:
    print(i)
