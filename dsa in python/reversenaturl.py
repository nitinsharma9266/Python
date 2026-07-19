"""def fun(n):
    if(n==0):
        return 
    print(n)
    fun(n-1)
        
n=int(input("enter number :"))
fun(n)
"""
#nth odd natural numbers
def fun(n):
    if(n==0):
        return 
    
    fun(n-1)
    print(2*n-1)
        
n=int(input("enter number :"))
fun(n)

#nt even nnumbers
def fun(n):
    if(n==0):
        return 
    
    fun(n-1)
    print(2*n)
        
n=int(input("enter number :"))
fun(n)

#nth odd reverse natural numbers
def fun(n):
    if(n==0):
        return 
    print(2*n-1)
    fun(n-1)
    
        
n=int(input("enter number :"))
fun(n)

#nt even reverse natural numbers
def fun(n):
    if(n==0):
        return 
    print(2*n)
    fun(n-1)
    
        
n=int(input("enter number :"))
fun(n)
