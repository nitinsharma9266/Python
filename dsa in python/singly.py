# ===========================================
# 👇 Singly Linked List Implementation in Python
# ===========================================

# Node class ek single node ko represent karta hai
# Har node me 'item' (data) aur 'next' (aage wale node ka address/reference) hota hai
class Node:
    def __init__(self, item=None, next=None):
        self.item = item      # Node ke andar store hone wala data
        self.next = next      # Next node ka reference (agar hai to)


# Singly Linked List (SLL) class
class SLL:
    def __init__(self, start=None):
        self.start = start    # Linked list ka first node (head) — shuru me None hota hai

    # Function: List empty hai ya nahi
    def is_empty(self):
        return self.start == None

    # Function: List ke start me ek new node insert karna
    def insert_at_start(self, data):
        n = Node(data, self.start)  # Naya node banaya jiska next = current start
        self.start = n              # Naya node ab starting node ban gaya

    # Function: List ke end (last) me ek new node insert karna
    def insert_at_last(self, data):
        n = Node(data)              # Naya node bana jiska next = None
        if not self.is_empty():     # Agar list empty nahi hai
            temp = self.start       # Temp variable se start se traversal start karte hain
            while temp.next is not None:  # Jab tak last node nahi milta
                temp = temp.next
            temp.next = n           # Last node ke next me naya node jod diya
        else:
            self.start = n          # Agar list empty thi, to naya node hi first node ban gaya

    # Function: Koi data search karna (mil gaya to node return karega)
    def search(self, data):
        temp = self.start
        while temp is not None:     # Jab tak list khatam nahi hoti
            if temp.item == data:   # Agar current node ka item match kar gaya
                return temp         # To us node ko return kar do
            temp = temp.next
        return None                 # Agar nahi mila to None return

    # Function: Kisi specific node ke baad ek naya node insert karna
    def insert_after(self, temp, data):
        if temp is not None:        # Agar diya gaya node exist karta hai
            n = Node(data, temp.next)  # Naya node bana jiska next = temp ke next
            temp.next = n              # Aur temp ka next ab ye naya node ho gaya

    # Function: List ke sabhi elements print karna
    def print_list(self):
        temp = self.start
        while temp is not None:     # Jab tak list khatam nahi hoti
            print(temp.item, end=" ")  # Current node ka data print karo
            temp = temp.next        # Next node pe jao

    # Function: Pehla node delete karna
    def delete_first(self):
        if self.start is not None:  # Agar list empty nahi hai
            self.start = self.start.next  # Pehla node hata do (start ko next node par set kar do)

    # Function: Last node delete karna
    def delete_last(self):
        if self.start is None:      # Agar list empty hai to kuch mat karo
            pass
        elif self.start.next is None:  # Agar list me sirf ek node hai
            self.start = None          # To use hata do (list empty ho gayi)
        else:
            temp = self.start
            # Jab tak second last node tak nahi pahuchte
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None         # Last node ko None kar diya (delete ho gaya)

    # Function: Specific item delete karna
    def delete_item(self, data):
        if self.start is None:  # Agar list empty hai
            pass

        elif self.start.next is None:  # Agar list me sirf ek node hai
            if self.start.item == data:
                self.start = None      # Wo ek node delete kar do

        else:  # Agar list me 2 ya zyada nodes hain
            temp = self.start

            # Agar first node hi delete karna hai
            if temp.item == data:
                self.start = temp.next
            else:
                # Middle ya last node delete karna
                while temp.next is not None:
                    if temp.next.item == data:  # Agar next node match karta hai
                        temp.next = temp.next.next  # Us node ko skip kar do (delete ho gaya)
                        break                       
                    temp = temp.next  # Next node par move karo
                    
    def __iter__(self):
        return SLLItrator(self.start)
class SLLItrator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data
    

# ===========================================
# 👇 Driver Code (Program ka main part)
# ===========================================

# SLL object banate hain
"""my_list = SLL()

# Starting me elements add karte hain
my_list.insert_at_start(20)   # List: 20
my_list.insert_at_start(10)   # List: 10 -> 20
my_list.insert_at_last(30)    # List: 10 -> 20 -> 30

# 20 ke baad 25 insert karte hain
my_list.insert_after(my_list.search(20), 25)  # List: 10 -> 20 -> 25 -> 30

# List print karte hain
print("Initial List:")
my_list.print_list()          # Output: 10 20 25 30
print()

# 20 ko delete karte hain
my_list.delete_item(30)

# Delete ke baad list print karte hain

for x in my_list:
    print(x,end=" ")

print()
"""