# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ret = 0
        while head:
            ret |= head.val
            ret <<= 1
            head = head.next

        return ret >> 1
        
