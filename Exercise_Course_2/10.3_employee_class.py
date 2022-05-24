'''
Employee class
'''

class Employee:
    company = "Google"
    salary = 100    

rashid = Employee()
yasir = Employee
# rashid.salary = 300
# yasir.salary = 400
print(rashid.company)
print(yasir.company)
Employee.company = "YouTube"
print(rashid.company)
print(yasir.company)
print(rashid.salary)
print(yasir.salary)