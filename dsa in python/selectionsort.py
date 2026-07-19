"""import time
start=time.time()

class SELECTION:
    def __init__(self,items):
        self.items=items
        
    def sort(self):
        n=len(self.items)
        
        for i in range(n-1):
            min_index=i
            for j in range(i+1,n):
           
                if(self.items[j]<self.items[min_index]):
                    min_index=j
            # self.items[i],self.items[min_index]=self.items[min_index],self.items[i]
            temp=self.items[i]
            self.items[i]=self.items[min_index]
            self.items[min_index]=temp
                        
    def print_bsort(self):
        print("sorted array")
        for x in self.items:
            print(x,end=" ")
end=time.time()        
print("%.6f sec"%(end-start))
data=[1,3,7,12,5,17]
b=SELECTION(data)
b.sort()
b.print_bsort()



"""

def selection_sort(list1):
    n=len(list1)
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if(list1[j]<list1[min_index]):
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]
                
l1=[64,35,89,21,72,13]

selection_sort(l1)
print(l1)
            
