# Write a class Train which has method to book a ticket get status (no of seats) and get fare information of train running under indian railwways
from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo
        
    def book(self,fro,to):
        print(f"Ticked is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    
    def getFare(self,fro,to):
        print(f"TIcket fare in train no:{self.trainNo} fro {fro} to {to} is {randint(222,5555)}")
        
        
t=Train(12342)   
t.book("Rewa","Bhopal")
t.getStatus() 
t.getFare("Rewa","Bhopal")