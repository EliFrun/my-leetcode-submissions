# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
depth = 101
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return
         
        global depth
        depth = n
        self.removeNthFromEnd(head.next, n)
        depth -= 1
        if depth == 0:
            head.next = head.next.next
            
        return head.next if depth == 1 else head
        
        
