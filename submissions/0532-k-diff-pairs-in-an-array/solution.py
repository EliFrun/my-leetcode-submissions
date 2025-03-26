class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        ret = 0
        if k == 0:
            return sum(1 for v in c.values() if v > 1)
        for i in set(nums):
            if i + k in c:
                ret += 1

        return ret
            
        
