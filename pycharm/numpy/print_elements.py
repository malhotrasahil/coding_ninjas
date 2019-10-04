## Open and read data file as specified in the question
## Print the required output in given format
import numpy as np
input_=np.arange(1,21,1)
input_=input_.reshape(4,5)


# print(input_)


print(*input_[2,:3])
print(*input_[1:4,3])
x=(input_[2:4,])
for i in x :
    for j in i :
        print(j, end=' ')
print()
y=(input_[1:3,1:3])
for i in y :
    for j in i :
        print(j, end=' ')

