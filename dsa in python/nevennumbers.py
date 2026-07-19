"""
N even numbers in order
def Neven(n):
    if(n==0):
        return 
    
    elif(n%2==0):
            Neven(n-1)
            print(n)     
    else:
        Neven(n-1)        
n=int(input("enter the number : "))
Neven(n)"""
# neven numbers in reverse order
def Neven(n):
    if(n==0):
        return 
    
    elif(n%2==0):
            print(n)     
            Neven(n-1)
            
    else:
        Neven(n-1)        
n=int(input("enter the number : "))
Neven(n)