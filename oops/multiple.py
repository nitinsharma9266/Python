class employee:    # this is my child class 1.
    company="ITC"
    name="Nitin"
    def show(self):
        print(f"the name is employee {self.name} and the company is {self.company}")
    
class coder:     # this is my child class 2.
    language="python"
    def printlanguage(self):
        print(f"out of all the language here is your language {self.language}")
    

class programmer(employee,coder):   #this is my parent class.
    company="ITC INFO Tech"

    def showlanguage(self):
        print(f"the name is employee {self.company} and he is good with {self.language} language")

a=employee()
b=programmer()

b.show()
b.printlanguage()
b.showlanguage()

