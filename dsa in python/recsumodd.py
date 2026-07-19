"""
sum of first odd n natural number by recursion 

def sum(n):
    if(n==0 ):
        return 0 
    elif(n%2!=0):
        return n+sum(n-1)
        
    else:
        return sum(n-1)
n=int(input("enter natural numbers : "))
r=sum(n)
print(r)
"""
# sum of first even n natural numbers by racursion

"""def sum(n):
    if(n==0 ):
        return 0 
    elif(n%2==0):
        return n+sum(n-1)
        
    else:
        return sum(n-1)
n=int(input("enter natural numbers : "))
r=sum(n)
print(r)"""

# nth odd natural numbers sum
def sum(n):
    if(n==1 ):
        return 1 
    return 2*n-1+sum(n-1)
n=int(input("enter natural numbers : "))
S=sum(n)
print(S)

# nth even natural numbers sum
def sum(n):
    if(n==1 ):
        return 2 
    return 2*n+sum(n-1)
n=int(input("enter natural numbers : "))
S=sum(n)
print(S)