class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        ret = 0
        for key in sorted(c.keys()):
            if key + 1 in c:
                ret = max(ret, c[key] + c[key + 1])

        return ret

            
        
