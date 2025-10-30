class Solution:
    def numWays(self, s: int, arrLen: int) -> int:        
        @cache
        def solve(pos, left):
            if left == 0:
                return 1 if pos == 0 else 0
            ret = solve(pos, left - 1)
            if pos < arrLen - 1:
                ret += solve(pos + 1, left - 1)
            if pos != 0:
                ret += solve(pos - 1, left - 1)
            return ret % 1_000_000_007

        return solve(0, s)
        

        
