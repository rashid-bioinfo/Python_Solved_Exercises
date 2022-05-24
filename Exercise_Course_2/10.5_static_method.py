'''
Static method
'''

class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary of the employee working in {self.company} is {self.salary} \n{signature}")
    
    @staticmethod
    def greet(signature):
        print(f"Good morning sir\n{signature}")


rashid = Employee()
rashid.salary = 40000
rashid.getSalary("Thanks")
rashid.greet("Thanks")
