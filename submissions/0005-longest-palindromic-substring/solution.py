class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPal(f):
            return f[:len(f)//2] == "".join(reversed(list(f[(len(f) + 1)//2:])))
        
        if not s:
            return s
        
        m = 1
        ret = s[0]
        for i in range(1, len(s)):    
            if s[i] == s[i - 1]:
                j = 1
                while i - j - 1 >= 0 and i + j < len(s) and s[i - j - 1] == s[i + j]:
                    j += 1
                
                j -= 1
                if 2 + 2 * j > m:
                    m = 2 + 2 * j
                    ret = s[i - j - 1:i + j + 1]
            
            if i + 1 < len(s) and s[i - 1] == s[i + 1]:
                j = 1
                while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                    j += 1
                    
                j -= 1
                if 1 + 2 * j > m:
                    ret = s[i - j:i + j + 1]
                    m = 1 + 2 * j
                
                
        return ret
