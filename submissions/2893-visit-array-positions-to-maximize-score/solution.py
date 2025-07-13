class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        dp = [0] * len(nums)
        best_even = 0
        best_odd = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] & 1:
                dp[i] = nums[i] + max(best_odd, max(0, best_even - x))
                best_odd = max(best_odd, dp[i])
            else:
                dp[i] = nums[i] + max(best_even, max(0, best_odd - x))
                best_even = max(best_even, dp[i])

        return dp[0]
                
        
