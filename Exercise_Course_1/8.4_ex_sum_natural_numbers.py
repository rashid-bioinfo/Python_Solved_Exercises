'''
Write a recursive function to calucalte the sum of n natural numbers
'''

def sum_func_iter(n):
    mysum = 0
    for i in range(n):
        mysum = mysum + (i+1)
    return mysum

def sum_func_recur(n):
    if n == 1:
        return 1
    else:
        return n + sum_func_recur(n-1)

print(sum_func_iter(5))
print(sum_func_recur(5))