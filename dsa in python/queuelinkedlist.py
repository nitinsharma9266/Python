class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
        
    def is_empty(self):
        return self.front==None
    def enqueue(self,data):
        n=node(data)
        if self.is_empty():
            self.front=n
            self.rear=n
            
        else:
            self.rear.next=n
            self.rear=n
        self.item_count+=1
        
    def dequeue(self):
        if not self.is_empty():
            self.front=self.front.next
        
        elif(self.front==self.rear):
            self.front=None
            self.rear=None
            
        else:
            raise IndexError("queue underflow!")
        self.item_count-=1
        
    def get_front(self):
        if not self.is_empty():
            return self.front.item
        else:
            raise IndexError("Queue is underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.item
        else:
            raise IndexError("Queue is underflow")
        
    def size(self):
        if not self.is_empty():
            return self.item_count
        else:
            raise IndexError("No data in the queue!")
        
q1=Queue()


q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.dequeue()
print()











        
        
        
    
        
        
        
            