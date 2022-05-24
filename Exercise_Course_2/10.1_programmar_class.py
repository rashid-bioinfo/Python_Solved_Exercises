class Programmar:
    company = "Microsoft"
    salary = 100

    def getDetail(self):
        print(f"The name of the programmer working in {self.company} is: {self.name}")
        print(f"The salary of the {self.name} is: {self.salary}")

rashid = Programmar()
yasir = Programmar()
rashid.name = "Rashid"
rashid.salary = 200
rashid.getDetail()
yasir.name = "Yasir"
yasir.getDetail()