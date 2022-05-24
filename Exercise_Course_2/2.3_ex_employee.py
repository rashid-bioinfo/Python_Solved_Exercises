class Employee:
    salary = 4500
    SalaryIncrement = 100

    # @getter
    @property
    def salaryAfterIncrement(self):
        return self.salary + self.SalaryIncrement

    # @setter
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,val):
        self.SalaryIncrement = val - self.salary

e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 5100
print(e.salaryAfterIncrement)
print(e.SalaryIncrement)