from math import sqrt

a=float(input("Enter first number : "))
b=float(input("Enter second number : "))
c=float(input("Enter the third number : "))

d=b*b-4*a*c
if d>0:
    print("roots are real and different ")
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print("root1= ",r1)
    print("root2= ",r2)
elif d==0:
    print("root are real and equal")
    r1=r2=-b/(2*a)
    print("root1= ",r1)
    print("root2= ",r2)
else:
    
        
    print("roots are imaginry")
    
    