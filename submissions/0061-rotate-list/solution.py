# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        if k == 0:
            return head
        tail = None
        
        length = 0
        curr = head
        while curr:
            length += 1
            tail = curr
            curr = curr.next

        k = length - k % length
        if k == 0:
            return head

        tail.next = head
        curr = head
        for i in range(k - 1):
            curr = curr.next


        ret = curr.next
        curr.next = None
        return ret

        
        
