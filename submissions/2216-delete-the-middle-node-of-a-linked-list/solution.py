# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def len(node):
            if not node:
                return 0
            return 1 + len(node.next)

        length = len(head)
        if length == 1:
            return None
        def solve(node, idx):
            if idx == length // 2 - 1:
                node.next = node.next.next if node.next else None
                return
            solve(node.next, idx + 1)
        solve(head, 0)
        return head
        
