class Solution:
    
    def numDecodings(self, s: str) -> int:
        return self.helper({},s)
    
    
    
    def helper(self, memo, s):
        if not s:
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        ret = 0
        if int(s[0:2]) <= 26:
            if len(s) - 1 not in memo:
                memo[len(s) - 1] = self.helper(memo, s[1:])
            if len(s) - 2 not in memo:
                memo[len(s) - 2] = self.helper(memo, s[2:])
            ret += memo[len(s) - 1]
            ret += memo[len(s) - 2]
        else:
            if len(s) - 1 not in memo:
                memo[len(s) - 1] = self.helper(memo, s[1:])
            ret += memo[len(s) - 1]
            
        return ret
        
