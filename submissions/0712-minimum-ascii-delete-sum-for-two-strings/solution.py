class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        @cache
        def solve(i, j):
            if i >= len(s1):
                return sum(ord(c) for c in s2[j:])
            if j >= len(s2):
                return sum(ord(c) for c in s1[i:])

            if s1[i] == s2[j]:
                return solve(i + 1, j + 1)
            
            return min(
                ord(s1[i]) + solve(i + 1, j),
                ord(s2[j]) + solve(i, j + 1)
            )

        return solve(0, 0)

        
