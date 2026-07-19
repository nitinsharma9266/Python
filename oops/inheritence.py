class employee:
    company="ITC"
    def show(self):
        print(f"the name is employee {self.name} and the salary is {self.salary}")
    
# class programmer:
#     company="ITC INFO"

#     def show(self):
#         print(f"the name is employee {self.name} and the salary is {self.salary}")


#     def showlanguage(self):
#         print(f"the name is employee {self.name} and  he is good with {self.language} language")
class programmer(employee):
    company="ITC INFO"

    def show(self):
        print(f"the name is employee {self.name} and the salary is {self.salary}")

a=employee()
b=programmer()

print(a.company,b.company)