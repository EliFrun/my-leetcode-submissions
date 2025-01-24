# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = [(-1, 10 ** 10)]
        ret = []
        curr = head
        i = 0
        while curr:
            ret.append(0)
            if curr.val <= stack[-1][1]:
                stack.append((i, curr.val))
            else:
                while curr.val > stack[-1][1]:
                    ret[stack[-1][0]] = curr.val
                    stack.pop()
                stack.append((i, curr.val))
            i += 1
            curr = curr.next

        return ret
        
