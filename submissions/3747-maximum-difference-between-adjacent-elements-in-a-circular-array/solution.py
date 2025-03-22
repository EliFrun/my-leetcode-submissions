class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ret = 0
        for i in range(len(nums)):
            ret = max(ret, abs(nums[i] - nums[(i + 1) % len(nums)]))
        return ret
