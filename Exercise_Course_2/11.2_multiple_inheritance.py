class Employee:
    company = "Google"

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgrageLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Rashid"

# e = Employee()
p = Programmer()
print(p.level)
p.upgrageLevel()
print(p.level)