class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        coords = [None] * (len(grid) * len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                coords[grid[i][j]] = (i, j)

        for i in range(len(coords) - 1):
            curr_i, curr_j = coords[i]
            nxt_i, nxt_j = coords[i + 1]
            if abs(nxt_i - curr_i) not in [1,2] or abs(nxt_j - curr_j) not in [1,2]:
                return False
            if abs(nxt_i - curr_i) == 1 and abs(nxt_j - curr_j) != 2:
                return False
            if abs(nxt_i - curr_i) == 2 and abs(nxt_j - curr_j) != 1:
                return False

        return True
        
