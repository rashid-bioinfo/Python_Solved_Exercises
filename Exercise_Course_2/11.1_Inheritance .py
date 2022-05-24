class Employee:
    company = "Google"

    def getDetail(self):
        print("This is employee class")

class Programmer(Employee):
    language = "Python"
    company = "YouTube"

    def getLanguage(self):
        print(f"Programmer is learning {self.language}")

    def getDetail(self):
        print("This is progammer class")


e = Employee()
p = Programmer()
e.getDetail()
p.getDetail()
print(p.company)