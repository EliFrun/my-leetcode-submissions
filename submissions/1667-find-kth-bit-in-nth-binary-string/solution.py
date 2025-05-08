class Solution:
    def findKthBit(self, l: int, k: int) -> str:
        @cache
        def solve(n):
            if n == 1:
                return "0"
            return solve(n - 1) + "1" + "".join(["1" if x == "0" else "0" for x in solve(n - 1)][::-1])

        return solve(l)[k - 1]
        
