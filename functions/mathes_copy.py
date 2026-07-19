with open("copy.txt") as f:
    content1= f.read()

with open("this_copy.txt") as f:
    content2=f.read()

if(content1==content2):
    print("yes these contents are identical")

else:
    print("No these contents are not identical")