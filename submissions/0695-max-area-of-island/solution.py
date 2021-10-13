class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(curr, visited):
            if curr in visited:
                return 0
            i, j = curr
            ret = 1
            visited.add(curr)
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                ret += dfs((i - 1, j), visited)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                ret += dfs((i, j - 1), visited)
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                ret += dfs((i + 1, j), visited)
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                ret += dfs((i, j + 1), visited)
            return ret
        
        visited = set()
        ret = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == 1 and (i,j) not in visited:
                    ret = max(ret, dfs((i, j), visited))
 
                
        return ret
        
