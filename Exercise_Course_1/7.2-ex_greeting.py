'''
Greet the persons in the list using for loop
'''
mylist = ['Harry', 'Soham', 'Sachin', 'Rahul']

for item in mylist:
    if item.startswith("S"):
        print(str(item) + "! Welcome to learning Python")
    else:
        continue