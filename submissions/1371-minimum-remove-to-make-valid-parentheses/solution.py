class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = []
        stk = []
        
        
        for i,c in enumerate(s):
            if c == '(':
                stk.append((c,i))
            elif c  == ')':
                if stk and stk[-1][0] == '(':
                    stk.pop()
                else:
                    indexes_to_remove.append(i)
                    
        indexes_to_remove.extend([i for x,i in stk])
        indexes_to_remove.sort()
        s = list(s)
        for i in reversed(indexes_to_remove):
            s.pop(i)
        return ''.join(s)
