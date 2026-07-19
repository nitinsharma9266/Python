n=int(input("Enter a number: "))

count=0
while count<n:
    count=count+1
    if n%count==0:
        if count==n or count==1:
            continue
        else:
            print("Not a prime number")
            