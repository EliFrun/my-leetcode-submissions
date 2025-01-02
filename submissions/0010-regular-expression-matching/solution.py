class Solution:
    @functools.cache
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:])
            return len(p) == 0
        
        if len(p) == 0:
            return len(s) == 0

        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                if s[0] == p[0]:
                    return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
                else:
                    return self.isMatch(s, p[2:])
        elif p[0] == '.':
            return self.isMatch(s[1:], p[1:])
        else:
            return (self.isMatch(s[1:], p[1:]) if s[0] == p[0] else False)

        
        
