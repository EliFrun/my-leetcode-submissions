class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        @cache
        def solve(l, r):
            if r - l + 1 < 3:
                return 0
            ret = float('inf')
            for i in range(l + 1, r):
                ret = min(ret, values[l] * values[r] * values[i] + solve(l, i) + solve(i, r))
            return ret
        return solve(0, len(values) - 1)
