
class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary of the employee working in {self.company} is {self.salary}")

rashid = Employee()
yasir = Employee()
rashid.salary = 40000
yasir.salary = 35000

rashid.getSalary()
yasir.getSalary()
# Employee.getSalary(rashid)