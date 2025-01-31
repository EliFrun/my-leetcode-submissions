# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = []
        curr = headA
        while curr:
            setA.append(curr)
            curr = curr.next

        setB = []
        curr = headB
        while curr:
            setB.append(curr)
            curr = curr.next
        
        prev = None
        for a,b in zip(setA[::-1], setB[::-1]):
            if a != b:
                return prev

            prev = a

        return prev
            

        
        
