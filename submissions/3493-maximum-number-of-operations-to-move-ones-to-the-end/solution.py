class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        ret = 0
        for i in range(len(s)):
            if i + 1 < len(s) and s[i] == '0' and s[i + 1] == '0':
                continue
            if s[i] == '1':
                ones += 1
            else:
                ret += ones
        return ret
        
