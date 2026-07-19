marks1=int(input("enter your marks1: "))
marks2=int(input("enter your marks2: "))
marks3=int(input("enter your marks3: "))

total_marks=marks1+marks2+marks3

total_percentage=(total_marks*100)/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed! ")

else:
    print("failed! try again next year!")