'''
to check age with relational operators
'''

age = int(input("Please enter your age: "))

if (age > 18 and age < 34):
    print("Your age is between 18 and 34")
elif (age> 18 or age > 34):
    print("You are surely greater than 18")
else:
    print("your age is less than 18")
