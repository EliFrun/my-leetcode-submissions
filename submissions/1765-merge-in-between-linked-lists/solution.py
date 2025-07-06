# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = ListNode(-1, list1)
        curr = head
        i = 0
        end = None
        while i < a:
            curr = curr.next
            i += 1
        
        end = curr
        while i <= b:
            curr = curr.next
            i += 1
        start = curr.next

        curr = list2
        while curr.next:
            curr = curr.next
        
        curr.next = start
        end.next = list2
        return head.next
        
