class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def can(i, j):
            count_w = 0
            count_w += (1 if grid[i][j] == 'W' else -1)
            count_w += (1 if grid[i][j + 1] == 'W' else -1)
            count_w += (1 if grid[i + 1][j] == 'W' else -1)
            count_w += (1 if grid[i + 1][j + 1] == 'W' else -1)
            return count_w != 0
        
        for i in range(len(grid) - 1):
            for j in range(len(grid[0]) - 1):
                if can(i,j):
                    return True

        return False

        
