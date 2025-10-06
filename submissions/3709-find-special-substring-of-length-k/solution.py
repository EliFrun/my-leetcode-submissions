class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        curr = ''
        cnt = 0
        l = set()
        for c in s:
            if c == curr:
                cnt += 1
            else:
                curr = c
                l.add(cnt)
                cnt = 1
        
        l.add(cnt)
        return k in l
        
