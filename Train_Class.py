class Train():
    def __init__(self,name,fare,seats):
        self.name = name 
        self.fare = fare 
        self.seats = seats 
    def getFare(self):
        print(f"The Fare Of Train Is {self.fare}")
    def getStatus(self):
        print("--------------Train Info------------")
        print(f"Name Of Train Is {self.name}")
        print(f"Total Number Of Seats Available In {self.name} Is {self.seats}")
    def bookTicket(self):
        if(self.seats>0):
            print("-----------------------------------")
            print(f"You Ticket Have Book! And YOu Seat Number Is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("-------------------------------------")
            print("Sorry! No More Tickets Are Available")
    def cancelTicket(self):
        self.seats = self.seats + 1
        
        print(f"You Cancell YOur Ticket! {self.seats}")
intercity = Train("Hazara Express",100,90)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket()
intercity.getStatus()



