str=input()
list_counted=list()
max_occur_count=0
max_occur_char=''
for i in str:
    if str.count(i)>max_occur_count:
        max_occur_char=i
        max_occur_count=str.count(i)


print(max_occur_char)