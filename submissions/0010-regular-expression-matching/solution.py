class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def solve(i, j):
            if i == len(s):
                if len(p) - j > 1 and p[j + 1] == '*':
                    return solve(i, j + 2)
                return j == len(p) 

            if j == len(p):
                return i == len(s)
            
            
            if len(p) - j > 1 and p[j + 1] == '*':
                ret = solve(i, j + 2)
                if ret:
                    return True
                if s[i] == p[j] or p[j] == '.':
                    return solve(i + 1, j) or solve(i, j + 2) or solve(i + 1, j + 2)
            
            if p[j] == '.':
                return solve(i + 1, j + 1)
            
            if s[i] != p[j]:
                return False
            return solve(i + 1, j + 1)

        return solve(0, 0)
