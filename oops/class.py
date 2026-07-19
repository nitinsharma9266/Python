class employee:
    name="Sachin"   #This is a class attribute.
    language="python"
    salary=12000

Sachin=employee()  #This is a object attribute.
Sachin.name="sachin Sharma"
print(Sachin.name, Sachin.salary,Sachin.language)

Rohan=employee()
Rohan.name="Rohan roro robinson"
print(Rohan.name, Sachin.salary,Sachin.language)

# here name is a object attribute 
# and sallary is a class attribute as they directly belog to the class.