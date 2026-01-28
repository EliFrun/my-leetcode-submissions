class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        x = SortedList()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                x.add((grid[i][j], i, j))

        prev = [(float('inf'), float('inf'))]
        
        @cache
        def solve(i, j):
            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                return 0
            idx = bisect_left(prev, (grid[i][j], -1))
            ret = prev[idx][1]
            if i + 1 < len(grid):
                ret = min(ret, grid[i + 1][j] + solve(i + 1, j))
            if j + 1 < len(grid[0]):
                ret = min(ret, grid[i][j + 1] + solve(i, j + 1))
            return ret

        ret = float('inf')
        for _ in range(k + 1):
            ret = min(ret, solve(0, 0))
            prev = [(-1, float('inf'))]
            for v, i, j in x:
                if v == prev[-1][0]:
                    a,b = prev.pop(-1)
                    prev.append((a, min(b, solve(i, j))))
                else:
                    prev.append((v, min(prev[-1][1], solve(i, j))))

            solve.cache_clear()

        return ret
            
            
            
        
