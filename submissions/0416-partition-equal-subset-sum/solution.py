class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) & 1 == 1:
            return False
        
        nums.sort()
        @cache
        def solve(i, t):
            if t < 0:
                return False
            if t == 0:
                return True
            if i >= len(nums):
                return False

            return solve(i + 1, t - nums[i]) or solve(i + 1, t)

        return solve(0, sum(nums) // 2)
