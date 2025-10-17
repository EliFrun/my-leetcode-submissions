class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        @cache
        def solve(i, j, left):
            if i >= j:
                return 0 if i > j else 1
            if s[i] == s[j]:
                return 2 + solve(i + 1, j - 1, left)

            v = 0
            min_diff = min((ord(s[i]) - ord(s[j]) + 26) % 26, (ord(s[j]) - ord(s[i]) + 26) % 26)
            if min_diff <= left:
                v = 2 + solve(i + 1, j - 1, left - min_diff)
            return max(solve(i + 1, j, left), solve(i, j - 1, left), v)
        return solve(0,len(s) - 1,k)
