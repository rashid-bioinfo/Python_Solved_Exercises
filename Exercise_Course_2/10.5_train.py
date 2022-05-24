class Train:
    noOfSeats = 41
    fare = 500
    def bookTicket(self):
        Train.noOfSeats = Train.noOfSeats - 1
        print("Congratulations! Your seat has been reserved")

    def getStatus(self):
        print(f"{Train.noOfSeats} seats are available for booking")

    def getFare(self):
        print(f"Fare for traveling is {Train.fare}")

rashid = Train()
rashid.getStatus()
rashid.getFare()
rashid.bookTicket()
rashid.bookTicket()
rashid.getStatus()