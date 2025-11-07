# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        curr_ret = ret

        curr = head.next
        while curr:
            s = 0
            while curr.val != 0:
                s += curr.val
                curr = curr.next
            curr = curr.next
            curr_ret.next = ListNode(s)
            curr_ret = curr_ret.next
        return ret.next
            
        
        
