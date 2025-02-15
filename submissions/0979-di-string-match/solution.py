class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ret = []
        l = 0
        u = len(s)
        for c in s:
            if c == 'I':
                ret.append(l)
                l += 1
            else:
                ret.append(u)
                u -= 1
        ret.append(u)
        return ret
        
