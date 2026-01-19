class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @cache
        def solve(i, j):
            if i >= len(grid):
                return 0
            ret = 1e9
            for jj, v in enumerate(moveCost[grid[i][j]]):
                ret = min(ret, grid[i][j] + (v if i != len(grid) - 1 else 0) + solve(i + 1, jj))
            return ret

        return min(solve(0, j) for j in range(len(grid[0])))

        
