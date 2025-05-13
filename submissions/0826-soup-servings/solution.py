class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1
        @cache
        def solve(i, j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1
            if j <= 0:
                return 0
            
            return 0.25 * solve(i - 100, j) + 0.25 * solve(i - 75, j - 25) + 0.25 * solve(i - 50, j - 50) + 0.25 * solve(i - 25, j - 75)

        return solve(n,n)
        
