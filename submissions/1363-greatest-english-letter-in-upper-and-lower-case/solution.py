class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for i in range(26):
            c = chr(ord('Z') - i)
            if c in s and c.lower() in s:
                return c
        return ""
        
