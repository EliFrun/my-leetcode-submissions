# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
        
        
        nums = []
        
        for node in lists:
            while node:
                nums.append(node.val)
                node = node.next
                
        
        nums.sort()
        
        ret = ListNode()
        current = ret
        for num in nums:
            current.next = ListNode(num)
            current = current.next
            
        return ret.next
