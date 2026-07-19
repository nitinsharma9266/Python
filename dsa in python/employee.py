class Employee:
    
    def __init__(self,empid=None,name=None,salary=None):
        self.empid=empid
        self.name=name
        self.salary=salary
        
    def setempid(self,empid):
        self.empid=empid
    def setname(self,name):
        self.name=name
    def setsalary(self,salary):
        self.salary=salary   
        
    def getempid(self):
        return self.empid
    def getname(self):
        return self.name
    def getsalary(self):
        return self.salary
    
e1=Employee()
e2=Employee(1,"ramesh",30000)
e1.setempid(2)
e1.setname("mahesh")
e1.setsalary(200000)
print(e1.getempid(),e1.getname(),e1.getsalary())
print(e2.getempid(),e2.getname(),e2.getsalary())