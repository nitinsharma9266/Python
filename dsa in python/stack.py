class Stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        
            return self.items.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return IndexError("stack is empty")
        
    def size(self):
        return len(self.items)
    
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("top element",s1.peek())
print("removed element",s1.pop())
print("top element",s1.peek())
print()
            