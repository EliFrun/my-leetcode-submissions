# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        while curr:
            if curr.next.next == None:
                curr.val = curr.next.val
                curr.next = None
                break
            curr.val = curr.next.val
            curr = curr.next

        
        
