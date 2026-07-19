def sos(n):
    if(n==0):
        return 0
    return n*n+sos(n-1)
n=int(input("enter number : "))
r=sos(n)
print(r)
