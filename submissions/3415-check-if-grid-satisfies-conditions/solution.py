class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        return all(
            [
                ''.join([str(i) for i in grid[0]]) == ''.join([str(i) for i in x]) for x in grid
            ]
        ) and all([grid[0][i - 1] != v for i,v in enumerate(grid[0]) if i != 0])
