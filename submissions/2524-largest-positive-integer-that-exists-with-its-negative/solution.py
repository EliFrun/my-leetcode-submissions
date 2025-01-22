class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        values = set()
        ret = -1
        for n in nums:
            if -n in values:
                ret = max(ret, abs(n))
            else:
                values.add(n)

        return ret
        
