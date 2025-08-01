class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        M = 1_000_000_007
        dp = [0,0,0]
        for num in nums:
            if num == 0:
                dp[num] = (2 * dp[num] + 1) % M
            else:
                dp[num] = (2 * dp[num] + dp[num - 1]) % M
        return dp[-1]
            
