class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            nonlocal visited
            if (i, j) in visited:
                return 0
            if grid[i][j] != 1:
                return 0
            
            visited.add((i, j))
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            ret = 1
            for di, dj in directions:
                if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                    ret += dfs(i + di, j + dj)
                    
            return ret
        
        
        best_area = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    best_area = max(best_area, dfs(i, j))
                    
        return best_area
