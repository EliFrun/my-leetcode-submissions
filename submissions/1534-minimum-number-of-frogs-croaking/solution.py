class Solution:
    def minNumberOfFrogs(self, s: str) -> int:
        # ends w: c r o a k
        states = [0,0,0,0,0]
        ret = 0
        for c in s:
            i = 'croak'.index(c)
            if i > 0:
                if states[i - 1] > 0:
                    states[i - 1] -= 1
                else:
                    return -1
            states[i] += 1
            ret = max(ret, sum(states[0:4]))
        return ret if sum(states[0:4]) == 0 else -1
                
        
        
