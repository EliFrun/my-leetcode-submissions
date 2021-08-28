# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = []
        
        curr = head
        
        while curr:
            n.append(curr)
            curr = curr.next
            
        ret_head = ListNode()
        curr = ret_head
        for i in range(len(n)//2):
            curr.next = n[i]
            curr = curr.next
            curr.next = n[-(1 + i)]
            curr = curr.next
         
        if len(n) % 2 != 0:
            curr.next = n[len(n) // 2]
            curr = curr.next
            
        curr.next = None
            
        return ret_head.next
