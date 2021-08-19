# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current_node = head
        node_with_curr_val = current_node
        current_val = head.val
        
        while current_node:
            if current_node.val != current_val:
                node_with_curr_val.next = current_node
                node_with_curr_val = current_node
                current_val = current_node.val
    
            current_node = current_node.next
        
        
        node_with_curr_val.next = None
                
            
            
        return head
                
