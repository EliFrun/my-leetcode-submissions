class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @functools.cache
        def count(s, t):
            if len(s) < len(t):
                return 0
            if t == "":
                return 1
            if s == "":
                return 0
            
            a = 0
            if s[0] == t[0]:
                a = count(s[1:], t[1:])

            return a + count(s[1:], t)

        return count(s, t)
        
