class Number:

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Decimal number is {self.number}"

n = Number(9)
print(n)