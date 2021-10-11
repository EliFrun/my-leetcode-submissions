class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return reduce(lambda x, y: x + len([i for i in y if i < 0]), grid, 0)
        
