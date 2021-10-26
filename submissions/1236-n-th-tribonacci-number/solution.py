class Solution:
    def tribonacci(self, n: int) -> int:
        ret = [0, 1, 1]
        while n > 2:
            ret.append(ret[0] + ret[1] + ret[2])
            ret.pop(0)
            n -= 1
            
        return ret[n]
        
        
        
