from random import randint

class Train:

    def __init__(slf,trainNO):
        slf.trainNO=trainNO
         
    def book(Nitin,fro,to):
       print(f"Ticket is booked in train no: {Nitin.trainNO} from {fro} to {to}")

    def getstatus(self):
        print(f" train no: {self.trainNO} is running on time.")

    def getFare(self,fro,to):
        print(f"ticket fare in train no :{self.trainNO} from {fro} to {to} is {randint(222,5555)}")    
        
t=Train(12399)
t.book("Rampur","Delhi")
t.getstatus()
t.getFare("Rampur","Delhi")