class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([sum([1 if x < 0 else 0 for x in row]) for row in grid])
        
