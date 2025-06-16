class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ret = -1
        m = float('inf')
        for num in nums:
            ret = max(num - m, ret)
            m = min(m, num)

        return ret if ret > 0 else -1
        
