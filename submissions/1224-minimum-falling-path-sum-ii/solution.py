class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        grid = [sorted([(v, i) for i,v in enumerate(x)])[:3] for x in grid]
        @cache
        def solve(prev, i):
            if i >= len(grid):
                return 0
            ret = float('inf')
            for v, idx in grid[i]:
                if prev == idx:
                    continue
                ret = min(ret, v + solve(idx, i + 1))

            return ret

        return solve(-1, 0)
        
