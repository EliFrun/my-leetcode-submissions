# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        
        curr = head
        while curr:
            if id(curr) in s:
                return True
            s.add(id(curr))
            curr = curr.next
            
        return False
