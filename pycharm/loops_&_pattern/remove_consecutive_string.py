str=input()

x=''
temp=''
for a in range(len(str)):
    if temp==str[a]:
        temp = str[a]
        continue
    else:
        x +=str[a]
        temp = str[a]

print(x)

