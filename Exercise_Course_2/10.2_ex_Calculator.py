import math

class Calculator:
    
    def square(self):
        return self.num * self.num
    
    def cube(self):
        return self.num * self.num * self.num
    
    def sqroot(self):
        return math.sqrt(self.num)

    @staticmethod
    def greet():
        print("hello")

       

calc = Calculator()
calc.greet()
calc.num = int(input("Please enter a number: "))
sq_out = calc.square()
print(f"The square of {calc.num} is {sq_out}")
cb_out = calc.cube()
print(f"The cube of {calc.num} is {cb_out}")
sr_out = calc.sqroot()
print(f"The cube of {calc.num} is {sr_out}")