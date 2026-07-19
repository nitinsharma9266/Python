count=0
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count==2:
        print(i)
    count=0
    



    