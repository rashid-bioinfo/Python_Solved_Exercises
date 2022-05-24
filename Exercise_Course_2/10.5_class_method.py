
class Employee:

    name = "Rashid"
    salary = 100
    location = "Lahore"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

e = Employee() 
print(e.salary)
e.changeSalary(200)
print(e.salary)
print(Employee.salary)
