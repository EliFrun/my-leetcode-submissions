class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        ret = 1
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
            if grid[i][0] <= k:
                ret += 1
            else:
                pass
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
            if grid[0][j] <= k:
                ret += 1
            else:
                pass

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += grid[i][j - 1] + grid[i - 1][j] - grid[i - 1][j - 1]
                if grid[i][j] <= k:
                    ret += 1
                else:
                    pass
        return ret
        
