class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        sr = s[::-1]
        @cache
        def solve(i, j):
            if i >= len(s):
                return 0
            if j >= len(sr):
                return 0

            if s[i] == sr[j]:
                return 1 + solve(i + 1, j + 1)
            return max(
                solve(i + 1, j),
                solve(i, j + 1)
            )
        return solve(0, 0)
