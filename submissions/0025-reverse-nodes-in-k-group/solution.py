# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        
        foo = ListNode()
        
        foo.next = head
        foo_tracker = foo
        
        curr = head
        
        while curr:
            lis = []
        
            for i in range(k):
                if curr:
                    lis.append(curr)
                    curr = curr.next
                else:
                    break
                
            if len(lis) < k:
                break
            
            print([x.val for x in lis])
            
            poo = ListNode()
            curr_rev = poo
            for n in reversed(lis):
                curr_rev.next = n
                curr_rev = curr_rev.next
                
            curr_rev.next = curr
            
            foo_tracker.next = poo.next
            foo_tracker = curr_rev
            
        return foo.next
            
