class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def solve(house_1_robbed, i):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1:
                return 0 if house_1_robbed else nums[i]

            if i == 0:
                return max(solve(False, i + 1), nums[0] + solve(True, i + 2))
            return max(solve(house_1_robbed, i + 1), nums[i] + solve(house_1_robbed, i + 2))

        return solve(False, 0)

        
