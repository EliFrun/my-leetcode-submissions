class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        for i in range(len(grid)):
            lis = []
            x, y, j = i, 0, 0
            while x + j < len(grid) and y + j < len(grid[0]):
                lis.append(grid[x + j][y + j])
                j += 1

            lis.sort()

            x, y, j = i, 0, 0
            while x + j < len(grid) and y + j < len(grid[0]):
                grid[x + j][y + j] = lis[-j -1]
                j += 1

        for i in range(1, len(grid[0])):
            lis = []
            x, y, j = 0, i, 0
            while x + j < len(grid) and y + j < len(grid[0]):
                lis.append(grid[x + j][y + j])
                j += 1

            lis.sort()

            x, y, j = 0, i, 0
            while x + j < len(grid) and y + j < len(grid[0]):
                grid[x + j][y + j] = lis[j]
                j += 1
        
        return grid
