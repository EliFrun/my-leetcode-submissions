class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        dp = [[[0] * (maxMove + 1) for _ in range(n)] for __ in range(m)]
        
        dp[startRow][startColumn][0] = 1
        dirs = [0,1,0,-1,0]
        for k in range(maxMove - 1):
            for i in range(m):
                for j in range(n):
                    for l in range(4):
                        di, dj = dirs[l], dirs[l + 1]
                        if not 0 <= i + di < m:
                            continue
                        if not 0 <= j + dj < n:
                            continue
                        dp[i + di][j + dj][k + 1] += dp[i][j][k]
        
        ret = 0
        for i in range(m):
            ret += sum(dp[i][0]) + sum(dp[i][-1])

        for j in range(n):
            ret += sum(dp[0][j]) + sum(dp[-1][j])
        return ret % 1_000_000_007
