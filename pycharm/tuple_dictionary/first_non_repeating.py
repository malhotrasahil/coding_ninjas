def nonRepeatingChar(string):
    # set_string=set(string)
    # print(set_string)
    dict = {}
    for e in string:
        dict[e] = dict.get(e, 0) + 1
    # print (dict)

    for i in string :
        if dict[i]==1:
            return i



# Main
string = input()
# string='paannjshsdiksjsnnnnn'
print(nonRepeatingChar(string))
