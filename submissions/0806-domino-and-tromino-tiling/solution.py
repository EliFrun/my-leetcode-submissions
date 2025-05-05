class Solution:
    def numTilings(self, m: int) -> int:
        @cache
        def solve(full, left):
            if left <= 0:
                return 0
            if left == 1:
                return 1 if full else 0
            if left == 2:
                return 2 if full else 1
            if full:
                return 2 * solve(False, left - 1) + solve(True, left - 1) +  solve(True, left - 2)
            return solve(False, left - 1) + solve(True, left - 2)

        return solve(True, m) % 1_000_000_007

        
