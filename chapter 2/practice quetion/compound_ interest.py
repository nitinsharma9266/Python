p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=int(input("Enter the time in years: "))

'''#using for loop
for i in range(t):
    print("Year",i+1,":",p*(1+r/100)**(i+1))'''
# without using for loop

A=p*(1+r/100)**t

Compound_interest=A-p

print("The compound interest is:",Compound_interest)
print("The total amount after",t,"years is:",A)