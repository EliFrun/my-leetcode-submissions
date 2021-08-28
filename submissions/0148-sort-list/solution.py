# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        return self.helper(head, length)
            
        
        
    def helper(self, head, size):
        if size == 0:
            return head
        if size == 1:
            return head
        if size == 2:
            if head.val < head.next.val:
                head.next.next = None
                return head
            else:
                foo = head.next
                foo.next = head
                head.next = None
                return foo
            
        curr = head
        for i in range(size // 2 - 1):
            curr = curr.next
            
        second_half = curr.next
        curr.next = None
        sorted_first = self.helper(head, size // 2)
        sorted_second = self.helper(second_half, size - size // 2)
        
        
        ret = ListNode()
        curr = ret
        while sorted_first and sorted_second:
            if sorted_first.val > sorted_second.val:
                curr.next = sorted_second
                sorted_second = sorted_second.next
            else:
                curr.next = sorted_first
                sorted_first = sorted_first.next
            
            curr = curr.next
            
        if sorted_first:
            curr.next = sorted_first
        if sorted_second:
            curr.next = sorted_second
            
        return ret.next
        
