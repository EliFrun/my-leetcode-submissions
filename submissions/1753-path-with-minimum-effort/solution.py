class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int: 
        # djikstra

        q = [(0, 0, 0)]
        dirs = [0,1,0,-1,0]
        dp = [[float('inf')] * len(heights[0]) for _ in heights]

        while q:
            effort, i, j = heappop(q)
            if dp[i][j] <= effort:
                continue
            if i == len(heights) - 1 and j == len(heights[0]) - 1:
                return effort
            dp[i][j] = effort
            for k in range(4):
                di, dj = dirs[k:k + 2]
                if not 0 <= i + di < len(heights):
                    continue
                if not 0 <= j + dj < len(heights[0]):
                    continue
                heappush(q, (max(effort, abs(heights[i + di][j + dj] - heights[i][j])), i + di, j + dj))

        return dp[-1][-1]
        
        
