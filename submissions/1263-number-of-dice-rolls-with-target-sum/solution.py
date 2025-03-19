class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def solve(nn, tt):
            if tt < 0:
                return 0
            if nn > tt:
                return 0
            if nn == 1:
                return 1 if tt <= k else 0
            if nn == tt:
                return 1

            ret = 0
            for i in range(1, k + 1):
                ret += solve(nn - 1, tt - i)
            return ret

        return solve(n, target) % 1_000_000_007
        
