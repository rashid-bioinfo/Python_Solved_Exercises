'''
Greet the persons in the list using for loop
'''
mylist = ['Harry', 'Soham', 'Sachin', 'Rahul']

i = 0
while i < len(mylist):
    if mylist[i].startswith("S"):
        print(str(mylist[i])+"! Welcome to learning ") 
        i += 1
    else:
        i += 1
        continue