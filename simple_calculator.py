a=int(input("Enter the first number : "))
b=int(input("enter the second number : "))
z=input("Enter any sign +,-,%,*,/ : ")
if z=="+":
    print("sum of a and b will be ",a+b)
elif z=="-":
    print("sub of a and b will be ",a-b)
elif z=="*":
    print("mul of a and b will be ",a*b)
elif z=='/':
    print("div of a and b will be ",a/b)
    
elif z=="%":
    print("mod of a and b will be ",a%b)
elif z=="//":
    print("floor div of a and b will be ",a//b)
else:
    print("invailid input")