class Solution:
    def minDeletions(self, s: str) -> int:
        l = sorted([-x for x in Counter(s).values()])
        heapify(l)
        ret = 0
        while l:
            v = heappop(l)
            if v == 0:
                continue
            while l and l[0] == v:
                ret += 1
                heappush(l, heappop(l) + 1)
        return ret
        
        
