# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ret = ListNode(-1, head)
        curr = ret
        while curr:
            nxt = curr.next
            while nxt and nxt.val == val:
                nxt = nxt.next
            curr.next = nxt
            curr = curr.next

        return ret.next
        
