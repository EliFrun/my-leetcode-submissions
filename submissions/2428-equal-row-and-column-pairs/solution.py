class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = defaultdict(int)
        for row in grid:
            row_count[tuple(row)] += 1

        column_count = defaultdict(int)
        for j in range(len(grid)):
            s = tuple([grid[i][j] for i in range(len(grid))])
            column_count[tuple(s)] += 1

        ret = 0
        for k in set(row_count.keys()).intersection(column_count.keys()):
            ret += row_count[k] * column_count[k]

        return ret

        
