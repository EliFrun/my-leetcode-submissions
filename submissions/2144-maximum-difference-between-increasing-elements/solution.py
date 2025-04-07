class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mi = 2_000_000_000
        ret = -1
        for num in nums:
            if num - mi > ret:
                ret = num - mi
            mi = min(num, mi)

        return ret if ret > 0 else -1
    
