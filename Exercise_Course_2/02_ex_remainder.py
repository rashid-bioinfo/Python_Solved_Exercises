'''
Find remainder when a number is divided by 2
'''

num = int(input("Enter the number for finding remainder: "))

quotient = num/2
remainder = num%2
print("Quotient of %s is: %s" %(num, int(quotient)))
print("Remainder of %s is: %s" %(num, remainder))