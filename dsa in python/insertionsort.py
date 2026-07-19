"""def insertion_sort(list1):
    n=len(list1)
    for i in range(n-1):
        
        for j in range(i+1,n):
            if list1[j]<list1[i] and i>=0:
                temp=list1[j]
                list1[j]=list1[i]
                list1[i]=temp"""
                
def insertion_sort(list1):
    n=len(list1)
    for i in range(1,n):
        temp=list1[i]
        
        j=i-1
        while j>=0 and temp<list1[j]:
            list1[j+1]=list1[j]
            j-=1
        list1[j+1]=temp
            
l1=[25,37,11,14,60,82,18,41]
insertion_sort(l1)               
print(l1)
                
            
            