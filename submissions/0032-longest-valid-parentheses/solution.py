class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        ret = 0
        for i, c in enumerate(s):
            if c == "(":
                stk.append([1, False])
            if c == ")":
                if not stk:
                    continue
                if not stk[-1][1]:
                    stk[-1][0] += 1
                    stk[-1][1] = True
                elif stk[-1][1] and len(stk) == 1:
                    ret = max(ret, stk[-1][0])
                    stk = []
                elif len(stk) > 1 and not stk[-2][1]:
                    stk[-2][0] += 1 + stk.pop()[0]
                    stk[-1][1] = True
                while len(stk) > 1 and stk[-2][1]:
                    stk[-2][0] += stk.pop()[0]

        #print(stk)
        return max([x for x,b in stk if b] + [ret])
        
        

        
