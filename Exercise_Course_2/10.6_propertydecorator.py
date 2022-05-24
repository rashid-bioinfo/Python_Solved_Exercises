class Employee:
    salary = 4500
    salaryBonus = 500
    # @getter
    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    # @setter
    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary


e = Employee()
print(e.totalSalary)
e.totalSalary = 5200
# e.totalSalary = 5200  --> will throw an error (AttributeError: can't set attribute)
print(e.totalSalary)
print(e.salaryBonus)
