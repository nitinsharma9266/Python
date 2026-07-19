name = input("enter the name :")
marks = int(input("enter the marks : "))
phonenumber = int(input("enter phone number :"))

student = "Name of the student is {name} and physics marks is {marks} and student phone number {phonenumber}".format(
    name=name, marks=marks, phonenumber=phonenumber
)

print(student)
