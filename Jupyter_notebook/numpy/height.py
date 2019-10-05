import numpy as np

## Open and read data file as specified in the question
## Print the required output in given format
age=np.array([15,17,19,20,14,21,16,19,13,20,22,23,21,16,18,19,20,15,17,18])
height=np.array([156,144,180,162,152,157,154,155,151,150,158,179,126,182,183,154,159,160,172,149])


temp=np.where(height>155)

# print(age[temp])
a=age[temp]
h=height[temp]
#
# print(a)
# print(h)
for i in range(len(a)):
    print (str(a[i]) +' '+str(h[i]))