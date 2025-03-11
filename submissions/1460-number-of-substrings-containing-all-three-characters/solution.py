class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_a = -1 
        last_b = -1
        last_c = -1
        ret = 0
        for i,c in enumerate(s):
            if c == 'a':
                ret += max(0, min(last_b, last_c) + 1)
                last_a = i
            if c == 'b':
                ret += max(0, min(last_a, last_c) + 1)
                last_b = i
            if c == 'c':
                ret += max(0, min(last_a, last_b) + 1)
                last_c = i
        return ret
        
