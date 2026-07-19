class vector:
    def __init__(self,j,i,k):
        self.r=i
        self.i=j
        self.k=k

    def __add__(self,other):
        return vector(self.i+other.i+self.j+other.j+self.k+other.k)
    
    def __mul__(self,other):
        result=self.i*other.i+self.j*other.j+self.k*other.k


    def __str__(self):
        return f"Vector {self.r}i,{self.i}j,{self.k}k"
    
v=vector(2,4,8)
v2=vector(5,7,9)
v3=vector(1,3,5)
print(v+v2)
print(v*v2)

print(v+v3)
print(v*v3)