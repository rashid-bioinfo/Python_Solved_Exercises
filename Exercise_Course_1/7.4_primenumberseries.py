'''
Find prime number from 1 to 10
'''
mylist = []
for i in range(1,11):
    if (i%i == 0 and i%1 == 0 and i%2 != 0 and i%3 != 0):
        mylist.append(i)
    else:
        continue
print(mylist)