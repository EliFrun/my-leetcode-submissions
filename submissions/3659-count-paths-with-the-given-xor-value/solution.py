class Solution:
    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
        dp = [
                [[0] * 16 for __ in range(len(grid[0]))] for _ in range(len(grid))
            ]
        dp[0][0][grid[0][0]] = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for l in range(16):
                    if i - 1 >= 0:
                        dp[i][j][l ^ grid[i][j]] += dp[i - 1][j][l]
                    if j - 1 >= 0:
                        dp[i][j][l ^ grid[i][j]] += dp[i][j - 1][l] 


        return dp[-1][-1][k] % 1_000_000_007
