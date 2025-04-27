# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i,l in enumerate(lists):
            if l:
                h.append((l.val, i))

        heapify(h)
        ret = ListNode()
        curr = ret
        while h:
            _, idx = heappop(h)
            n = lists[idx]
            curr.next = n
            curr = n
            if n.next:
                lists[idx] = n.next
                heappush(h, (n.next.val, idx))
        
        return ret.next
        
