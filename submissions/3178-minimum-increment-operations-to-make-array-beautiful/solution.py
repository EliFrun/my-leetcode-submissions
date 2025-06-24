class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        @cache
        def solve(i):
            if i >= len(nums):
                return 0

            best = max(0, k - nums[i]) + solve(i + 3)
            if i > 1:
                best = min(best, max(0, k - nums[i - 2]) + solve(i + 1))
            if i > 0:
                best = min(best, max(0, k - nums[i - 1]) + solve(i + 2))
            #if i < len(nums) - 1:
            #    best = min(best, max(0, k - nums[i + 1]) + solve(i + 4))
            #if i < len(nums) - 2:
            #    best = min(best, max(0, k - nums[i + 2]) + solve(i + 5))
            return best

        return min(solve(0), solve(1), solve(2))
        
