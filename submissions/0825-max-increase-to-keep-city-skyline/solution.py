class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        sum = 0
        max_bottom = deepcopy(grid[0])
        max_left = []
        
        for row in grid:
            max_left.append(max(row))
            i = 0
            for column in row:
                max_bottom[i] = column if column > max_bottom[i] else max_bottom[i]
                i += 1
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #grid[i][j] = min(max_left[i], max_bottom[j])
                sum +=  max(0, min(max_left[i], max_bottom[j]) - grid[i][j])
        
        return sum
