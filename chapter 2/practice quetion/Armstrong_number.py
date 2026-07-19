num=int(input("Enter a number: "))


arm=0
c=num
while num>0:
    rem=num%10
    arm=arm+rem**3
    num=num//10

if c==arm:
    print("The number is an Armstrong number")
else:
    print("The number is not an Armstrong number")