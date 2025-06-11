class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        
        ret = s
        for i in range(len(s)):
            ret = min(ret, s[i:] + s[:i])
        return ret
        
