class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x,y,p in prices:
            dp[x][y] = max(dp[x][y], p)
        
        for i in range(m + 1):
            for j in range(n + 1):
                for ii in range(i//2 + 1):
                    dp[i][j] = max(dp[i][j], dp[ii][j] + dp[i - ii][j])
                for jj in range(j//2 + 1):
                    dp[i][j] = max(dp[i][j], dp[i][jj] + dp[i][j - jj])
        
        return dp[-1][-1]
                
        
