class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = [sum(grid[i]) for i in range(len(grid))]
        columns = [sum([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]

        n = len(rows)
        m = len(columns)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = 2 * rows[i] + 2 * columns[j] - n - m

        return grid
        
