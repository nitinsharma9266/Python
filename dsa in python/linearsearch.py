def LinearSearch(list1,data):
    for i in range(len(list1)):
        if list1[i]==data:
            print("data is found at index",i)
            return
        
    print("data is not found")
            
            
list1=[25,16,18,40,90,60,10]
LinearSearch(list1,10)
