def BinarySearch(list1,data):
    low=0
    high=len(list1)-1
    while low<=high:
        mid=low+(high-low)//2
        if data==list1[mid]:
            return mid
        elif data<list1[mid]:
            
            high=mid-1
        else:
            low=mid+1
    return -1       
    
list1=[10,16,18,25,40,60,90]

result=BinarySearch(list1,40)
print(result)