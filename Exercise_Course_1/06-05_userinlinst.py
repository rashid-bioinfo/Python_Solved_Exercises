'''
Check whether user is present in the list or not
'''

name = input("Please input your name: ")

name_list = ['rashid', 'yasir', 'sibtain']

if (name in name_list):
    print("The entered name is present in the list")
else:
    print("The entered name is NOT present in the list")