class Solution:
    def numTilings(self, m: int) -> int:
        mod = 10 ** 9 + 7
        @functools.cache
        def solve(n):
            nonlocal mod
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 5
            if n == 4:
                return 11
            return ((2 * solve(n - 1)) % mod + solve(n - 3) % mod) % mod

        return solve(m)
        
