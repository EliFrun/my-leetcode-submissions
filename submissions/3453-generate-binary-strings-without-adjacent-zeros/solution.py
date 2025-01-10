class Solution:
    def validStrings(self, n: int) -> List[str]:
        @functools.cache
        def solve(rem, prev0):
            if rem == 0:
                return [""]
            if prev0:
                return ["1" + x for x in solve(rem - 1, False)]
            return ["0" + x for x in solve(rem - 1, True)] + ["1" + x for x in solve(rem - 1, False)]

        return solve(n, False)
            
