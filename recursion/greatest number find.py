def greatest_number(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    
    else:
        return c


a=int(input("enter number a : "))
b=int(input("enter number b : "))
c=int(input("enter number c : "))
result=greatest_number(a,b,c)
print("greatest number is : ",result)
