"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        visiting = [root]
        to_visit = []
        while visiting:
            right = visiting[-1]
            for i in range(len(visiting) - 2, -1, -1):
                visiting[i].next = right
                right = visiting[i]
            
            for n in visiting:
                n.left and to_visit.append(n.left)
                n.right and to_visit.append(n.right)
            visiting = to_visit
            to_visit = []
            
        return root
