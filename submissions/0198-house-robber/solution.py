class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def solve(i):
            if i >= len(nums):
                return 0
            return max(nums[i] + solve(i + 2), solve(i + 1))

        return solve(0)
