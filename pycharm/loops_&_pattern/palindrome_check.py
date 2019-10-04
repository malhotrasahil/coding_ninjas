str=input()
len=len(str)
len_by_2= len//2
out="false"
j=len-1
for i in range(0,len_by_2):
    #for j in range(len-1, len_by_2-1,-1):
    if str[i]==str[j]:
        j=j-1
        continue
    else:
        break
else:
    out="true"
print(out)










