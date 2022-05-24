class Employee:
    company = "Google"

    def __init__(self):
        # print(f"Welcome") 

    def getDetail(self):
        print(f"The company of {self.name} is {Employee.company}")
        print(f"The company of {self.name} is {self.company}")

rashid = Employee()
rashid.name = "Rashid"
rashid.company = "YouTube"
rashid.getDetail()
Employee.company = "YouTube"
rashid.getDetail()

