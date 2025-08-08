class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1.0
        @cache
        def solve(a, b):
            if b <= 0 and a > 0:
                return 0
            if b <= 0 and a <= 0:
                return 0.5
            if a <= 0:
                return 1

            return (solve(a - 100, b) + solve(a - 25, b - 75) + solve(a - 50, b - 50) + solve(a - 75, b - 25)) / 4

        return solve(n, n)
        
