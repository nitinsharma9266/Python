class employee:
    language="python"    # this is an class attribute.
    salary=12000

    def __init__(self,name,salary,language):     # this method is dondor method.Which is automatically called.double space.
        self.name=name
        self.salary=salary
        self.language=language
        
        print("I am creating an object")



    def getInfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
        print("good morning !")

Sachin=employee("Sachin",13000,"javascript")
Sachin.name="Sachin"
print(Sachin.name,Sachin.salary,Sachin.language)

