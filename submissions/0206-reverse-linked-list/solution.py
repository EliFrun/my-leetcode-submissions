# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, h: Optional[ListNode]) -> Optional[ListNode]:

        ret = None
        def solve(curr):
            nonlocal ret
            if not curr:
                return None
            if curr.next is None:
                ret = ListNode(curr.val)
                return ret
            
            tail = solve(curr.next)
            tail.next = curr
            curr.next = None
            return curr
        solve(h)
        return ret
        
