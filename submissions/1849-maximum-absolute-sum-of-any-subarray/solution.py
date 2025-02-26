class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mi = 0
        ma = 0
        curr = 0
        for n in nums:
            curr += n
            mi = min(mi, curr)
            ma = max(ma, curr)

        return ma - mi

        
