'''
Calculate factorial
'''

def factorial_iter(n):
    fac = 1
    for i in range (1,n+1):
      fac = fac * i
    return fac

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

out1 = factorial_iter(5)
out2 = factorial_recursive(5)

print("factorial calculated through loop: ", out1)
print("factorial calculated through recursion: ", out2)
