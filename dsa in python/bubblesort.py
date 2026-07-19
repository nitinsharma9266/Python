import time
start=time.time()

class Bubble:
    def __init__(self,items):
        self.items=items
        
    def sort(self):
        n=len(self.items)
    
        for i in range(n-1):
            swapped=False
            for j in range(n-1-i):
                if(self.items[j]>self.items[j+1]):
                    temp=self.items[j]
                    self.items[j]=self.items[j+1]
                    self.items[j+1]=temp
                    swapped=True
            if not swapped:
                break    
    def print_bsort(self):
        print("sorted array")
        for x in self.items:
            print(x,end=" ")
    end=time.time()        
    print("%.20f sec"%(end-start))
data=[1,3,7,12,5,17]
b=Bubble(data)
b.sort()
b.print_bsort()
            
