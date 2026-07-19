class Deque:
    def __init__(self):
        
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    def insert_front(self,data):
        self.items.insert(0,data) 
        
    def insert_rear(self,data):
        self.items.append(data)
        
    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty !")
        else:
            self.front.pop(0)
            
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty !")
        else:
            self.front.pop()
            
    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty !")
        else:
            return self.items[0]
            
    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque underflow !")
        else:
            return self.items[-1]
            
    def size(self):
        if self.is_empty():
            raise IndexError("deque is empty !")
        else:
            return self.items
        
q1=Deque()
try:
    q1.size()
except IndexError as e:
    print(e)
q1.insert_front(10)
q1.insert_front(20)
q1.insert_rear(30)
q1.insert_rear(40)
print("front element is ",q1.get_front(),"rear element is ",q1.get_rear())
            
            
        