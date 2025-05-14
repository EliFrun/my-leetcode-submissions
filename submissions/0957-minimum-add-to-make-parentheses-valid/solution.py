class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = 0
        ret = 0
        for c in s:
            if c == '(':
                stk += 1
            else:
                stk -= 1
                if stk < 0:
                    stk = 0
                    ret += 1

        return ret + stk
        
