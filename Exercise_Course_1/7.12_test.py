
num = int(input("Please enter a number: "))
mylist = []
for i in range(2,num):
    if num%i == 0:
        print("The number is not prime number")
        mylist.append(num)
        num -= 1
        break
    else:
        print("the number is prime number")
        num -=1
        break
print(mylist, end="")