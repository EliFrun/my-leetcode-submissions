class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        curr = '0'
        count = 0
        ret = [0,0]
        for c in s:
            if c == curr:
                count += 1
            else:
                ret[int(curr)] = max(ret[int(curr)], count)
                count = 1
                curr = c

        ret[int(curr)] = max(ret[int(curr)], count)
        count = 1
        curr = c
        
        return ret[0] < ret[1]
        
