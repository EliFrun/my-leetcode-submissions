class Solution:
    def minAllOneMultiple(self, k: int) -> int:

        if k % 2 == 0 or k % 5 == 0:
            return -1
        n = 1
        v = 1
        while n <= k:
            if v % k == 0:
                return n
            v = (v * 10 + 1) % k
            n += 1
        return -1
            
        
