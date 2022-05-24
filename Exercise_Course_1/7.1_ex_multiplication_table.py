'''
Multiplication table using for loop
'''

num = int(input("Please input your number: "))

for i in range(1,11):
    print(str(i) + " x " + str(num) + " = " + str(i*num))