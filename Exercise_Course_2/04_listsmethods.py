'''
Lists methods
'''

mylist = [1,3,45,78,100,500,20,11,45]

print("Unsorted list: ", mylist)
mylist.sort() # sorts the list in ascending order
print("Sorted list in ascending order: ", mylist)
mylist.reverse() # sorts the list in descending order
print("Sorted list in descending order: ", mylist)
mylist.append("Rashid") # adds the value at the end of the list
print("Updated list: ", mylist)
mylist.insert(0,22)
print("Updated list: ", mylist)
mylist.pop(1) # will delete the value at 1st index i.e., 500
print("Updated list: ", mylist)
mylist.remove(20) # will delete the value 20
print("Updated list: ", mylist)

