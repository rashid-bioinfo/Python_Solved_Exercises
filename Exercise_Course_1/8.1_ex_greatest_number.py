'''
Write a function to find greatest of three numbers
'''

def greatest_number(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest_number(1000,60,10))