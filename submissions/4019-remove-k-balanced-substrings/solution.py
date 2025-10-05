class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stk = []
        for c in s:
            if c == '(':
                if stk and stk[-1] < 0:
                    stk[-1] -= 1
                else:
                    stk.append(-1)
            if c == ')':
                if stk and stk[-1] > 0:
                    stk[-1] += 1
                else:
                    stk.append(1)
            
            while stk and stk[-1] >= k:
                v = stk.pop()
                if stk:
                    u = stk.pop()
                else:
                    stk.append(v)
                    break
                if v + u < 0:
                    stk.append(v + u)
                elif v + u == 0:
                    pass
                else:
                    stk.append(u)
                    stk.append(v)
                    break
        
        ret = ""
        for n in stk:
            ret += ('(' if n < 0 else ')') * abs(n)
        return ret
