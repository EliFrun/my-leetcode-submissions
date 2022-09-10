"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        lis = []
        def navigate(node):
            nonlocal lis
            if not node:
                return
            
            lis.append(node)
            navigate(node.child)
            navigate(node.next)
        
        navigate(head)
        for i in range(len(lis) - 1):
            lis[i].next = lis[i+1]
            lis[i+1].prev = lis[i]
            lis[i].child = None
            
        lis[-1].child = None
        return head
        
