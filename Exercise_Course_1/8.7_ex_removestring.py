'''
Write a program to remove a given word from a list and strip it at the same time
'''
def strip_list(mylist):
    for item in mylist:
        if item == 'banana':
            mylist.remove('banana')
            mystr = item
    return mylist, mystr

out_list = strip_list(['mango', 'banana', 'apple'])
print("Original list which got stripped is here: ", out_list[0])
print("Stripped list from the original list is here:  ", out_list[1])
