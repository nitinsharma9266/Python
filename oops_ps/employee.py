class employee:
    salary=234
    increament=20


    @property
    def salaryafterincreament(self):
        return (self.salary+self.salary*(self.increament/100))
    

    @salaryafterincreament.setter
    def salaryafterincreament(self,salary):
        self.increament=((salary/self.salary)-1)*100
e=employee()
# print(e.salaryafterincreament)
e.salaryafterincreament=280.9
print(e.increament)
