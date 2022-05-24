class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        
        print("Employee object is created")
    
    def printDetail(self):
        print(f"Name of the employee is: {self.name}")
        print(f"Salary of the employee is: {self.salary}")
        print(f"Subunit of the employee is: {self.subunit}")

rashid = Employee("Rashid", 100, "YouTube")
rashid.printDetail()