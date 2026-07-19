class Demo:
    a=4


o=Demo()
print(o.a) #prints the class attribute because instance attribute is not present.

o.a=0  #instance attribute is set.

print(o.a) #prints the class instance attribute because instance attribute is  present.

print(Demo.a)  #prints the class attribute.
