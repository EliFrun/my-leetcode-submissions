class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        @cache
        def solve(i, j, left):
            if i >= len(grid):
                return float('-inf')
            if j >= len(grid[0]):
                return float('-inf')
            left -= (1 if grid[i][j] > 0 else 0)
            if left < 0:
                return float('-inf')
            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return grid[i][j]
            
            return grid[i][j] + max(solve(i + 1, j, left), solve(i, j + 1, left))
            
        return max(-1, solve(0,0,k))
