class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        dirs = [(-1,-1), (1,1), (-1,1), (1,-1)]
        valid_dirs = { 0: [0,2], 1: [1,3], 2: [1,2], 3: [0,3] }
        @cache
        def dfs(i,j,nxt,dir, can_change):
            if not 0 <= i < len(grid):
                return 0
            if not 0 <= j < len(grid[0]):
                return 0
            if grid[i][j] != nxt:
                return 0
            
            v = grid[i][j]
            grid[i][j] = -1
            ret = 0
            for d in valid_dirs[dir]:
                di, dj = dirs[d]
                if d != dir:
                    if not can_change:
                        continue
                ret = max(ret, dfs(i + di, j + dj, 2 - nxt, d, can_change and d == dir))

            grid[i][j] = v
            return 1 + ret
        ret = 0
        curr = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d, (di, dj) in enumerate(dirs):
                        ret = max(ret, 1 + dfs(i + di, j + dj, 2, d, True))

        return ret
                    
                            
                
        
