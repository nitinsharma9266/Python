class complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i

    def __add__(self,c2):
        return complex(self.r+c2.r,self.i+c2.i)


    def __str__(self):
        return f"{self.r}+{self.i}i"
    
c=complex(2,4)
c2=complex(5,7)
print(c+c2)
       