class Node:
    def __init__(self,item=None,prev=None,next=None):
        self.item=item
        self.prev=prev
        self.next=next
        
class CDLL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==None
    def insert_at_start(self,data):
        
        n=Node(data)
        if self.is_empty():     # ✅ अगर list खाली है
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next=self.start
            n.prev=self.start.prev
            self.start.prev.next=n
            self.start.prev=n
            self.start=n
            
    def insert_at_last(self,data):
        n=Node(data)
        if  self.is_empty():     # ✅ अगर list खाली है
            n.next = n
            n.prev = n
            self.start = n
            
        else:
            n.prev=self.start.prev
            n.next=self.start
            self.start.prev.next=n
            self.start.prev=n
    def search(self,data):
        if self.is_empty():
            return None
        else:
            temp=self.start
            while True:
                if temp.item==data:
                    return temp
                    break
                else:
                    temp=temp.next
            if temp.item==data:
                return temp
            else:
                return None
            
    def insert_after(self,temp,data):
            if temp  is None:
                return
            n=Node(data)
        
            n.prev=temp
            n.next=temp.next
            temp.next.prev=n
            temp.next=n
    def delete_first(self):
        if self.is_empty():
            return  # list already empty

    # अगर सिर्फ एक node है
        if self.start.next == self.start:
            self.start = None
        else:
        # normal case
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
        if self.start==None:
            return
        if self.start.next==self.start:
            self.start=None
        else:
            
            self.start.prev.prev.next=self.start
            self.start.prev=self.start.prev.prev
            
    def delete_item(self,data):
        if self.start is not None:
             
            temp=self.start
            if temp.item==data:
                self.delete_first()
            else:
                temp=temp.next
                while temp!=self.start:
                    if temp.item==data:
                        temp.next.prev=temp.prev
                        temp.prev.next=temp.next
    def __iter__(self):
        return CDLLItrator(self.start)

class CDLLItrator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        return data
                       
    def print_list(self):
        if not self.is_empty():
            temp = self.start
            while temp.next!= self.start:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item) 
            
        
            
my_list=CDLL()
my_list.insert_at_start(10) 
my_list.insert_at_last(20)  
my_list.insert_at_last(30)
my_list.insert_at_last(40)
my_list.insert_after(my_list.search(30),35) 
 # my_list.print_list()
  
for x in my_list:
    print(x,end=" ")
print()    
        