class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if max([int(x) for x in s]) > limit:
            return 0

        def solve(bound):
            if bound < int(s):
                return 0
            order = int(log10(bound))
            if order == len(s) - 1:
                return 1 if int(s) <= bound else 0
            
            combos = (limit + 1) ** (order - len(s))
            digits = min(limit + 1, int(str(bound)[0]))
            ret = combos * digits
            if int(str(bound)[0]) <= limit: 
                ret += solve(int(str(bound)[1:]))
            return ret
        
        return int(solve(finish) - solve(start - 1))
                



        
        

            

