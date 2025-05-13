class Solution:
    def concatenatedBinary(self, n: int) -> int:
        @cache
        def solve(i):
            if i == 1:
                return 1
            return (i + (solve(i - 1) << int(log2(i) + 1))) % 1_000_000_007

        return solve(n)
        
