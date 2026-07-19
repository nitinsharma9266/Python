a=int(input("enter a number : "))
b=int(input("enter a number : "))


if (b==0):
    raise ZeroDivisionError("hey i am good")
else:

    print(f"the division a/b is {a/b}")
