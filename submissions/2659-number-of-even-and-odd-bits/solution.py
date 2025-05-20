class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        i = 0
        ret = [0,0]
        while n > 0:
            ret[i] += n & 1
            i = 1 - i
            n >>= 1

        return ret

        
        
