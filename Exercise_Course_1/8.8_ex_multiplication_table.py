'''
Write a function to print multiplication table of a given number
'''
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")

multiplication_table(5)
print("\n")
multiplication_table(10)