class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        lis = list(senate)
        a = senate.count('R')
        b = senate.count('D')
        c = 0
        d = 0
        while a > 0 and b > 0:
            ch = lis.pop(0)
            if ch == 'R':
                if c > 0:
                    c -= 1
                    continue
                b -= 1
                d += 1
                lis.append(ch)
            if ch == 'D':
                if d > 0:
                    d -= 1
                    continue
                a -= 1
                c += 1
                lis.append(ch)

        return 'Radiant' if a > 0 else 'Dire'


        
