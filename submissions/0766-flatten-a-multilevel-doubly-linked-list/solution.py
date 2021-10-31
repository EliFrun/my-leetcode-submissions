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
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        nodes = []
        def navigate(node):
            if not node:
                return []    
            ret = [node] + navigate(node.child) + navigate(node.next)
            return ret
        
    
        nodes = navigate(head)

        for i, node in enumerate(nodes):
            if i < len(nodes) - 1:
                nodes[i + 1].prev = node
                node.next = nodes[i + 1]

            node.child = None


        return nodes[0]
        
