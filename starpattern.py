x=7

for i in range(x):
    if i==0 or i==(x-1):
        print("*" *x)
    else:
        print("*" + (x-2) *" "+ "*")
        
a=10
for i in range(a//2,a+1,2):
    print(" "*((a-i)//2) + "*" *i + " "*(a-i) + "*" *i)
    
for i in range(a,0,-1):
    print(" " * (a-i) + "*" * (2*i-1))
    