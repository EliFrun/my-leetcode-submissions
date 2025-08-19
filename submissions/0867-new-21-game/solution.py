class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + maxPts)
        for i in range(k, n + 1):
            dp[i] = 1
        
        prefix = n - k + 1
        for i in range(k - 1, -1, -1):
            dp[i] = prefix / maxPts
            prefix += dp[i]
            prefix -= dp[i + maxPts]

        return min(1.0, dp[0])
        
