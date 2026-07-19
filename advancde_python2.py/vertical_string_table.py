#it will be print table in horizontal 

# n=int(input("enter a number :" ))

# Table=[i*n for i in range(1,11)]

# with open("table.txt","a") as f:
#     f.write(f"Table of {n} :{str(Table)}\n")

# it will print a table in vartical 
n = int(input("enter a number :" ))

with open("table.txt", "a") as f:
    f.write(f"Table of {n}:\n")
    for i in range(1, 11):
        f.write(f"{i} x {n} = {i*n}\n")
    f.write("\n")  # Table ke baad ek blank line
