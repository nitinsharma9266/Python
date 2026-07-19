try:
    a=int(input("enter the number :"))
    print(a)

except ValueError as v:
    print(v)

else:
    print("I am inside the else ")   # this is executed only if the try was successful.
    