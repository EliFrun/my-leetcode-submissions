# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = ListNode()
        odd_head = ListNode()
        even_curr = even_head
        odd_curr = odd_head
        curr = head
        i = 0
        while curr:
            if i & 1:
                odd_curr.next = curr
                odd_curr = odd_curr.next
            else:
                even_curr.next = curr
                even_curr = even_curr.next
            curr = curr.next
            i += 1

        even_curr.next = odd_head.next
        odd_curr.next = None
        return even_head.next


        
