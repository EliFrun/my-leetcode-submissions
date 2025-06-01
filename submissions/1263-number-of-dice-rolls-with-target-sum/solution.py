class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n)]

        for j in range(1, k + 1):
            if j > target:
                break
            dp[0][j] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                for l in range(1, k + 1):
                    if j + l > target:
                        break
                    dp[i][j + l] = (dp[i][j + l] + dp[i - 1][j]) % 1_000_000_007


        return dp[-1][target]

        
