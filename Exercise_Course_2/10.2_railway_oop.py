class RailwayForm:
    formType = "Railway form"
    def printData(self):
        print(f"The applicat's name is {self.name}")
        print(f"The applicat's train is {self.train}")
    
rashidApplication = RailwayForm()
rashidApplication.name = "Rashid"
rashidApplication.train = "Tezgam"
rashidApplication.printData()