# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        tmp = ListNode()
        tmp.next = head
        
        current_node = tmp
        i = 0
        
        left_node = None
        foo = []
        while i <= right:
            if i + 1 == left:
                left_node = current_node
            if i >= left:
                foo.append(current_node)
            current_node = current_node.next
            i += 1
            
        right_node = current_node
            
            
            
        rev = ListNode()
        cur_rev = rev
        foo.reverse()
        
        for i in foo:
            cur_rev.next = i
            cur_rev = cur_rev.next
            
            
        left_node.next = rev.next
        cur_rev.next = right_node
        
        return tmp.next
