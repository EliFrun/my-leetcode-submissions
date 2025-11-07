class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        path_length = 0
        starting = (0,0)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    starting = (i, j)
                if grid[i][j] == 0:
                    path_length += 1
                
        
        def solve(i, j, num_steps):
            if i < 0: return 0
            if j < 0: return 0
            if i >= len(grid): return 0
            if j >= len(grid[0]): return 0
            if grid[i][j] == -1:
                return 0
            if grid[i][j] == 2:
                return 1 if path_length == num_steps else 0

            grid[i][j] = -1
            dirs = [0,1,0,-1,0]
            ret = 0
            for k in range(4):
                di, dj = dirs[k], dirs[k + 1]
                ret += solve(i + di, j + dj, num_steps + 1)
            grid[i][j] = 0
            return ret

        return solve(*starting,-1)
