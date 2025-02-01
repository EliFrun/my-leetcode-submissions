class Solution:
    def titleToNumber(self, s: str) -> int:
        ret = 0
        p = 0
        for c in s[::-1]:
            ret += (26 ** p) * (ord(c) - ord('A') + 1)
            p += 1

        return ret
        
