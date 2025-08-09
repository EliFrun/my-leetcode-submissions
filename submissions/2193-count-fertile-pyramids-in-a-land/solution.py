class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        def solve(gr):
            ret = 0
            for i in range(1, len(gr)):
                for j in range(1, len(gr[0]) - 1):
                    if gr[i][j]:
                        gr[i][j] = 1 + min(gr[i - 1][j - 1], gr[i - 1][j], gr[i - 1][j + 1])
                        ret += max(0, gr[i][j] - 1)
            return ret

        return solve(deepcopy(grid[::-1])) + solve(grid)
        
