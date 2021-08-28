"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # inefficient solution
        d = {}
        curr = head
        
        d_head = Node(-10001)
        d_curr = d_head
        
        i = 0
        while curr:
            d_curr.next = Node(curr.val)
            d_curr = d_curr.next
            d[i] = d_curr
            i += 1
            curr = curr.next
            
        d[i] = None
        
        curr = head
        d_curr = d_head.next
        
        
        while curr:
            d_curr.random = d[self.getIndex(curr.random, i)]
            d_curr = d_curr.next
            curr = curr.next
            
            
        return d_head.next
            
            
            
    def getIndex(self, n, length):
        i = 0
        
        while n:
            i += 1
            n = n.next
            
        return length - i
