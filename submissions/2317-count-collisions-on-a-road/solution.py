class Solution:
    def countCollisions(self, directions: str) -> int:
        stk = []
        ret = 0
        for d in directions:
            if d == 'L':
                if stk:
                    v = stk.pop()
                    if v == 'S':
                        ret += 1
                    else:
                        ret += 2
                        while stk and stk[-1] == 'R':
                            stk.pop()
                            ret += 1
                    stk.append('S')
            elif d == 'S':
                while stk and stk[-1] == 'R':
                    ret += 1
                    stk.pop()
                stk.append('S')
            else: # d == R
                stk.append(d)

        return ret
        
