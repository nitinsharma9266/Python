file_name="example.txt"
with open(file_name,"w+") as file:
    file.write("this is a content which is written i w+ mode\n")
    file.write("this is a class in which sit 56 students in this class ")
    """file.seek(0)
    content=file.read()
    print("file content after writting ")
    print(content)"""
    
with open(file_name,"r") as file:
    print("veriefied content this file")
    print(file.read())