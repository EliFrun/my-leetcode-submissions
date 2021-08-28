# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        lis = []
        
        while curr:
            lis.append((curr.val, curr))
            curr = curr.next
            
        lis = sorted(lis, key=lambda x: x[0])
        
        dummy = ListNode()
        curr = dummy
        
        for l in lis:
            curr.next = l[1]
            curr = curr.next
            
        curr.next = None
            
        return dummy.next
        

        
