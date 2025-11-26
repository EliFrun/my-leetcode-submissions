class Solution:
    def numberOfPaths(self, grid: List[List[int]], K: int) -> int:
        dp = [[[0] * K for _ in grid[0]] for _ in grid]
        dp[0][0][grid[0][0] % K] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(K):
                    if i > 0:
                        dp[i][j][(k + grid[i][j])% K] = (dp[i][j][(k + grid[i][j])% K] + dp[i - 1][j][k]) % 1_000_000_007
                    if j > 0:
                        dp[i][j][(k + grid[i][j])% K] = (dp[i][j][(k + grid[i][j])% K] + dp[i][j - 1][k]) % 1_000_000_007
        return dp[-1][-1][0] % 1_000_000_007
        
