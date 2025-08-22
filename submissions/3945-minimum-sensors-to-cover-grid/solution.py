class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        @cache
        def solve(nn, mm):
            if nn <= 0:
                return 0
            if mm <= 0:
                return 0
            
            return 1 + solve(nn - 2 * k - 1, 2 * k + 1) + solve(nn, mm - 2 * k - 1)

        return solve(n, m)
        
