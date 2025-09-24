class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        m = float('-inf')
        for num in nums:
            if num > m:
                m = num
        
        if m < 0:
            return m

        # need to find largest array
        # kadanes
        curr = 0
        ret = 0
        for num in nums:
            if curr + num > 0:
                curr = curr + num
            else:
                curr = 0
            if curr > ret:
                ret = curr

        best = ret

        # need to find smallest array to remove
        # kadanes
        curr = 0
        ret = 0
        for num in nums:
            if curr + num < 0:
                curr = curr + num
            else:
                curr = 0

            if curr < ret:
                ret = curr

        return max(best, sum(nums) - ret)
