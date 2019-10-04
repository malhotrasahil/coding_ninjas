## Open and read data file as specified in the question
## Print the required output in given format
# file=open("C:\\Users\\Sahil\\Downloads\\Sample.txt")
# print(file.read(100))
# for i in range(5):
#     print(file.readline())

with open("C:\\Users\\Sahil\\Downloads\\Sample.txt") as file:
    l1=file.readlines()
for i in range(5):
    print(l1[i])


# year2017.csv