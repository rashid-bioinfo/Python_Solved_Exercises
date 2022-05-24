'''
find the greatest of 4 numbers
'''
num1 = int(input("Please enter number, 1: "))
num2 = int(input("Please enter number, 2: "))
num3 = int(input("Please enter number, 3: "))
num4 = int(input("Please enter number, 4: "))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1 > f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")

# Method 2 for finding greatest number
# if num1 > num2 and num1 > num3 and num1 > num4:
#     print(num1, "is the greatest number")
# elif num2 > num1 and num2 > num3 and num2 > num4:
#     print(num2, "is the greatest number")
# elif num3 > num1 and num3 > num2 and num3 > num4:
#     print(num3, "is the greatest number")
# elif num4 > num1 and num4 > num2 and num4 > num3:
#     print(num4, "is the greatest number")

# Method 3 for finding greatest number
# if num1 > num2 and num1 > num3 and num1 > num4:
#     greatest = num1
# if num2 > num1 and num2 > num3 and num2 > num4:
#     greatest = num2
# if num3 > num1 and num3 > num2 and num3 > num4:
#     greatest = num3
# if num4 > num1 and num4 > num2 and num4 > num3:
#     greatest = num4
    
# print(greatest)

# Method 4 for finding greatest number
# if num1 > num2:
#     if num1 > num3:
#         if num1 > num4:
#             print (num1, "is greater")
# if num2 > num1:
#     if num2 > num3:
#         if num2 > num4:
#             print (num2, "is greater")
# if num3 > num1:
#     if num3 > num2:
#         if num3 > num4:
#             print (num3, "is greater")
# if num4 > num1:
#     if num4 > num2:
#         if num4 > num3:
#             print (num4, "is greater")