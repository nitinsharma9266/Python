class PriorityQ:
    def __init__(self):
        self.list=[]
        
    def push(self,data,priority):
        index=0
        while index<len(self.list) and self.list[index][1]<=priority:
            index+=1
        self.list.insert(index,(data,priority))
        
    def is_empty(self):
        return len(self.list)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("priority queue is empty")
        return self.list.pop(0)[0]
        
    def size(self):
        return len(self.list)
    
p=PriorityQ()
p.push(20,6)
p.push(23,3)
p.push(13,8)
p.push(89,0)
p.push(40,4)
p.push(10,2)
p.push(9,5)

while not p.is_empty():
    print(p.pop())