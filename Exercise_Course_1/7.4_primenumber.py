'''
Find a prime number 
'''

num = int(input("Pleae enter your number: "))
f1= 0
for i in range (1,20):
    if num%i == 0:
        f1 += 1
    else:
        continue
if f1 == 2:
    print(num, "is a prime number")
else:
    print(num, "is NOT a prime number")