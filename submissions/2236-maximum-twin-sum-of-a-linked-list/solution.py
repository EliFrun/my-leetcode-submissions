# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        lis = []
        curr = head
        while curr:
            lis.append(curr.val)
            curr = curr.next

        return max([a + b for a,b in zip(lis[:len(lis)//2], lis[len(lis) - 1:len(lis)//2 -1: -1])])
