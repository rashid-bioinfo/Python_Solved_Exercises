class Person:
    country = "Pakistan"

    def __init__(self):
        print("Intializing Person class ....\n")
        

    def takeBreath(self):
        print("I am taking breath...")

class Employee(Person):
    company = "Google"

    def __init__(self):
        super().__init__()
        print("Intializing Employee class...\n")

    def takeBreath(self):
        print("I am employee so I am taking breath")

class Programmer(Employee):

    def __init__(self):
        super().__init__()
        print("Intializing Programmer class...\n")

    def takeBreath(self):
        print("I am a programmer so I am breathing ++") 
        super().takeBreath()

    def getSalary(self):
        print(f"The salary of the employee is: {self.salary}")


# p = Person()
# p.takeBreath()

# e = Employee()
# e.takeBreath()

pr = Programmer()
# pr.takeBreath()
