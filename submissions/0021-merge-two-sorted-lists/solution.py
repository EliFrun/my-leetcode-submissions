# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(0)
        current = ret
        
        while(l1 is not None and l2 is not None):
            if l1.val < l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next
                
        if l1:
            while l1:
                current.next = l1
                current = current.next
                l1 = l1.next
        if l2:
            while l2:
                current.next = l2
                current = current.next
                l2 = l2.next
            
        return ret.next
