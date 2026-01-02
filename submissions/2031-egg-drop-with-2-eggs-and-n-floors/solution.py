class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        @cache
        def solve(v):
            if v == 1:
                return 1
            ret = float('inf')
            for i in range(v - 1, 0, -1):
                ret = min(ret, max(v - i, 1 + solve(i)))

            return ret

        return solve(n)
