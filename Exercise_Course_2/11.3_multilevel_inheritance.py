class Person:
    country = "Pakistan"

    def takeBreath(self):
        print("I am taking breath...")

class Employee(Person):
    company = "Google"

    def takeBreath(self):
        print("I am employee so I am taking breath")

class Programmer(Employee):

    def getSalary(self):
        print(f"The salary of the employee is: {self.salary}")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.country)
g = Programmer()
print(g.country)
print(g.company)
g.takeBreath()
