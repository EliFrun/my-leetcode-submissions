# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def solve(prev, node):
            if not node:
                return
            ret = None
            if node.next == None:
                ret = node
            elif node.next != None:
                ret = solve(node, node.next)
            node.next = prev
            return ret

        return solve(None, head)
        
