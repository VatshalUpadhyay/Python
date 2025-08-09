from random import randint
class Train:
    def __init__(self,TrainNo):
        self.TrainNo=TrainNo

    def book(self,fro,to):
        print(f"Ticket is booked in train number: {self.TrainNo}\nfrom {fro} to {to}")
    
    def getstatus(self):
        print(f"The Train number: {self.TrainNo} is running on time.")

    def getFare(self,fro,to):
        print(f"Ticket fare in train number: {self.TrainNo} from {fro} to {to} is {randint(2,554)}")


t=Train(12399)
t.book("Delhi","Deoria")
t.TrainNo=90999 # here you change the train number
t.getstatus()
t.getFare("Delhi","Deoria")
