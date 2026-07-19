def factorial(n):
    if(n==1 or n==0):   #base case
        return 1
    return n*factorial(n-1)

n=int(input("enter the number n : "))

print("factorial of number :",factorial(n))
 