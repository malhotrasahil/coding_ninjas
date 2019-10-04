import numpy as np

a=np.array(['a','b','c','d','e','f','g','h'])
# b=np.random.randint(0,7,8)


b=np.array([6, 0, 6, 6, 1, 0, 4, 1])

print(b)


arr=b>3
print(b[arr])
print(b[(b>3) & (b<5)])
c=b
c[2:5]=55
print(c)
c[c>15]=100
print(c)

ind=(np.where(c==100))
print(ind)

print(a[ind])



