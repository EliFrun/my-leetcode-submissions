class SegTree:
    def __init__(self, lis, lo, hi):
        self.hi = hi
        self.lo = lo
        self.left = None
        self.right = None
        if len(lis) > 1:
            self.left = SegTree(lis[:len(lis)//2], lo, lo + len(lis)//2 - 1)
            self.right = SegTree(lis[len(lis)//2:], lo + len(lis)//2, hi)
            self.max = self.left.max if self.left.max > self.right.max else self.right.max
            self.min = self.left.min if self.left.min < self.right.min else self.right.min
        else:
            self.max = lis[0]
            self.min = lis[0]
    
    def min_max_in_range(self, lo, hi):
        if self.lo > hi:
            return (float('inf'), -1)
        if self.hi < lo:
            return (float('inf'), -1)
        if lo <= self.lo and hi >= self.hi:
            return (self.min, self.max)
        
        l = self.left.min_max_in_range(lo, hi)
        r = self.right.min_max_in_range(lo, hi)

        return (l[0] if l[0] < r[0] else r[0]), (l[1] if l[1] > r[1] else r[1])

    def __str__(self):
        if self.left:
            print(self.left)
        if self.right:        
            print(self.right)
        return str(self.lo) + ' ' + str(self. hi)

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        s = SegTree(nums, 0, len(nums) - 1)
        q = []
        ret = 0
        for i in range(len(nums)):
            l, h = s.min_max_in_range(0, i)
            heappush(q, (l - h, (0, i)))

        for _ in range(k):
            v, (lo, hi) = heappop(q)
            ret -= v
            lo += 1
            l, h = s.min_max_in_range(lo, hi)
            if l <= h:
                heappush(
                    q,
                    (l - h, (lo, hi))
                )
        
        return ret

                
            
        
            
                
        
                    
            
        
