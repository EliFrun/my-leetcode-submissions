# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lis = ListNode()
        lis_head = lis
        
        after = ListNode()
        after_head = after
        
        current_node = head
        while current_node:
            if current_node.val < x:
                lis.next = current_node
                lis = lis.next
            else:
                after.next = current_node
                after = after.next
                
            current_node = current_node.next
            
        lis.next = after_head.next
        after.next = None
        return lis_head.next
