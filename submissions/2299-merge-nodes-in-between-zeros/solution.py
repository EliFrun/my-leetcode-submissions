# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret  = ListNode(0)
        tail = ret
        curr = head.next
        s = 0
        while curr:
            if curr.val == 0:
                tail.next = ListNode(s)
                s = 0
                tail = tail.next
            else:
                s += curr.val

            curr = curr.next
        return ret.next
