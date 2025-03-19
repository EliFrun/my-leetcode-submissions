class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        def solve(i, j, k):
            for m in range(i, i + k + 1):
                if grid[m][j] != 1 or grid[m][j + k] != 1:
                    return -1

            for m in range(j, j + k + 1):
                if grid[i][m] != 1 or grid[i + k][m] != 1:
                    return -1
            return (k + 1) * (k + 1)
                
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for k in range(min(len(grid) - i - 1, len(grid[0]) - j - 1) + 1):
                    ret = max(ret, solve(i, j, k))

        return ret
        
