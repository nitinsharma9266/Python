p1="make a lot of money"
p2="subscribe this"
p3="click this"
p4="buy now"

massage=input("enter your comment!")

if((p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage)):
    print("this is a spam!")

else:
    print("this is not a spam massage!")