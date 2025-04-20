class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[[0] * n for _ in range(3)] for j in range(2)]
        dp[0][0][n - 1] = 3
        dp[0][1][n - 1] = 3
        dp[0][2][n - 1] = 2
        dp[1][0][n - 1] = 2
        dp[1][1][n - 1] = 2
        dp[1][2][n - 1] = 1
        def solve(a, e, i):
            if i >= n:
                return 0
            if e > 2:
                return 0
            if a > 1:
                return 0
            if dp[a][e][i]:
                return dp[a][e][i]
            ret = (solve(a + 1, 0, i + 1) + solve(a, e + 1, i + 1) + solve(a, 0, i + 1)) % 1_000_000_007
            dp[a][e][i] = ret
            return dp[a][e][i]

        return solve(0, 0, 0) % 1_000_000_007
        
