class Solution:
    @functools.cache
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) > 0 and p[0] == '*':
                return self.isMatch(s, p[1:])
            return len(p) == 0
        
        if len(p) == 0:
            return len(s) == 0

        if p[0] == '?':
            return self.isMatch(s[1:], p[1:])

        if p[0] == '*':
            return self.isMatch(s[1:], p) or self.isMatch(s, p[1:])

        return self.isMatch(s[1:], p[1:]) if s[0] == p[0] else False

