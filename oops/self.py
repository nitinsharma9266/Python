class employee:
    language="python"    # this is an class attribute.
    salary=12000

    def getInfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
        print("good morning !")

Sachin=employee()
# sachin.lamguage="javascript"  #this is an instance attribute.
Sachin.greet()
Sachin.getInfo()

#  employee.getInfo(Sachin)