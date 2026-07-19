def inch_to_cent(n):
    n_1=2.542

    return n*n_1


n=int(input("enter inches : "))
a=inch_to_cent(n)
print(n,"inch is equal to ",a,"centimeter")