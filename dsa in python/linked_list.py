class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
a=Node(5)
b=Node(3)
c=Node(7)

a.next=b
b.next=c
head=a


print(head.data)
print(head.next.data)
print(head.next.next.data)

# traverse linked list
def print_list(self):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
# inertion at start
def insert_at_start(data):
    global head
    n=Node(data)
    n.next=head
    head=n        
def insert_at_end(data):
    curr=head
    n=Node(data)
    while curr.next!=None:
        curr=curr.next
    curr.next=n
def insert_after(data):

    k=3     
    n=Node(data)
    curr=head
    for i in range(k-1):
        curr=curr.next
    n.next=curr.next
    curr.next=n
def deletion_first():
    global head
    head=head.next 
    
def delete_last():
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    
def delete_item():
    k=2
    curr=head
    for i in range(k-1):
        curr=curr.next
    curr.next=curr.next.next
    
insert_at_start(4)
insert_at_end(1)
insert_after(6)
deletion_first() 
delete_last() 
delete_item()
print_list(head)


    