try:
    with open("file.txt1","r") as f:
        print(f.read())

except Exception as e:
    print(e)
                
try:
    with open("file.txt2","r") as f:
        print(f.read())

except Exception as e:
    print(e)
                
try:
    with open("file.txt3","r") as f:
        print(f.read())

except Exception as e:
    print(e)
                
print("Thank You !")