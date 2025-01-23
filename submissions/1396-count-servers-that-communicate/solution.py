import numpy

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def helper(row):
            count = 0
            for i in row:
                count += i
                if i > 1:
                    return count

            return count

        def helper2(idx):
            count = 0
            for i in range(len(grid)):
                count += grid[i][idx]
                if count > 1:
                    return count

            return count
        
        row_map = [sum(row) for row in grid]

        ret = 0
        for i, count in enumerate(row_map):
            if count > 1:
                ret += count
            elif count == 1:
                ret += 1 if helper2(grid[i].index(1)) > 1 else 0

        return ret
