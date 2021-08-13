# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current_node = head
         
        ret = ListNode()
        tracer_node = ret
        
        skipping = False
        while current_node:
            if current_node.next and current_node.next.val != current_node.val:
                if not skipping:
                    tracer_node.next = current_node
                    tracer_node = tracer_node.next
                skipping = False
            elif not current_node.next:
                    tracer_node.next = current_node if not skipping else None
            else:
                skipping = True
            
            current_node = current_node.next
                
        return ret.next
