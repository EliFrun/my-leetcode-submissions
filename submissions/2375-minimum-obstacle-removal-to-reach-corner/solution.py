class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        dp = [[float('inf')] * len(grid[0]) for _ in grid]
        q = [(0,0,0)]
        dirs = [0,1,0,-1,0]
        while q:
            m, i, j = heappop(q)
            if dp[i][j] <= m:
                continue
            dp[i][j] = m
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return m
            for k in range(4):
                di, dj = dirs[k:k + 2]
                if not 0 <= i + di < len(grid):
                    continue
                if not 0 <= j + dj < len(grid[0]):
                    continue
                if m + grid[i + di][j + dj] < dp[i + di][j + dj]:
                    heappush(q, (m + grid[i + di][j + dj], i + di, j + dj))

        return -1
                
        
