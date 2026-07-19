class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            digit = total % 10
            new_carry = total // 10
            
            node = ListNode(digit)
            
            node.next = add(
                l1.next if l1 else None,
                l2.next if l2 else None,
                new_carry
            )
            
            return node
        
        return add(l1, l2, 0)
