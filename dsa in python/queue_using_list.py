class Queue:
    def __init__(self):
        self.mylist=[]
        
    def is_empty(self):
        return len(self.mylist)==0
    
    def enqueue(self,data):
        self.mylist.append(data)
        
    def dequeue(self):
        if not self.is_empty():
            self.mylist.pop()
            
        else:
            raise IndexError("queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.mylist[0]
            
        else:
            raise Exception("queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.mylist[-1]
        else:
            raise Exception("queue is empty")
    def size(self):
        return len(self.mylist)
q1=Queue()
try:
    print(q1.get_front())
except Exception as e:
    print(e.args[0])
    
q1.enqueue(10)
q1.enqueue(29)
q1.enqueue(30)
q1.enqueue(40)
print("Front=",q1.get_front(),"Rear=",q1.get_rear())
try:
    q1.dequeue()
    print("queue has now ",q1.size(),"element")
except IndexError as e:
    print(e.args[0])
    