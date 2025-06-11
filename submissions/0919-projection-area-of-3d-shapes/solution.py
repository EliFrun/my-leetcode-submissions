class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ret = 0
        ret += sum([(sum([1 if x > 0 else 0 for x in l])) for l in grid])
        ret += sum([max(l) for l in grid])
        ret += sum([max([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))])
        return ret
        
