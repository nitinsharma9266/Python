n=int(input("Enter the number of elements you want to add in list: "))

fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
print("Factorial of",n,"is",fact)
