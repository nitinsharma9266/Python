"""
Nodd numbers in order 

def Nodd(n):
    if(n==0):
        return 
    
    elif(n%2!=0):
            
            Nodd(n-1)
            print(n)
    else:
        Nodd(n-1)        
n=int(input("enter the number : "))
Nodd(n)"""
# nodd numbers in reverse order 
def Nodd(n):
    if(n==0):
        return 
    
    elif(n%2!=0):
            print(n)
            Nodd(n-1)
            
    else:
        Nodd(n-1)        
n=int(input("enter the number : "))
Nodd(n)