class Employee:
    company = "Google"
    establishedSince = 35
    place = "University of Manchester"

    def display(self):
        print(f"The name is {self.name}, age is {self.age} and the place is {self.place}")



rashid = Employee()
yasir = Employee()
print(rashid.company)
print(yasir.company)
yasir.company = "YouTube"
print(yasir.company)
print(rashid.company)
Employee.company = "Facebook"
print(yasir.company)
print(rashid.company)
print(yasir.company)