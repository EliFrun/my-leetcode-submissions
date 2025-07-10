class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = Counter([t % 60 for t in time])
        ret = 0
        for k,v in c.items():
            if k > 30:
                continue
            elif k in (0, 30):
                ret += (v) * (v - 1) // 2
            else:
                ret += v * c[60 - k]   
            
        return ret
        
