# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = {}
        
        curr = head
        while curr:
            if id(curr) in s:
                return s[id(curr)]
            s[id(curr)] = curr
            curr = curr.next

        return None
