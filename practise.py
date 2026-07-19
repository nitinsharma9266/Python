from math import sqrt
x=int(input("Enter first number : "))
y=int(input("Enter the second number : "))
z=int(input("Enter the third number : "))

"""if x>y and x>z:
    print(x ," is greater ")
elif y>x and y>z:
    print(y ," is greater ")
elif z>x and z>y:
    print(z ,"is greater ")
else:
    print("All numbers are equal")
    """
    
if x>y:
    if x>z:
        print(x," is grater")
    else:
        print(z," is greater ")
else:
    if y>z:
        print(y," is greater ")
    else:
        print(z ,"is greater ")
        
print(sqrt(16))

        
        
    