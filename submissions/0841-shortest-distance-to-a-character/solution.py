class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        closest = 0
        for i,v in enumerate(s):
            if v == c:
                closest = i
                break
                
        ret = [0] * len(s)
        for i,v in enumerate(s):
            if v == c:
                closest = i
                
            ret[i] = abs(closest - i)
        
        closest = 0
        for i,v in enumerate(s[::-1]):
            if v == c:
                closest = len(s) - i - 1
                break
                
        rev_ret = [0] * len(s)
        for i,v in enumerate(s[::-1]):
            if v == c:
                closest = len(s) - i - 1
                
            rev_ret[len(s) - i - 1] = abs(closest - (len(s) - i - 1))
        
        
        for i in range(len(s)):
            ret[i] = min(ret[i], rev_ret[i])
        return ret
