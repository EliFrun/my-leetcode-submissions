class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        l = []
        prev = 0
        cnt = 0
        curr = '-'
        ret = 0
        for c in s:
            if c == curr:
                cnt += 1
            else:
                ret += min(prev, cnt)
                prev = cnt
                curr = c
                cnt = 1
        ret += min(prev, cnt)
        return ret
        
