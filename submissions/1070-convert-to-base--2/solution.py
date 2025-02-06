class Solution:
    def baseNeg2(self, n: int) -> str:
        ret = []
        if n == 0:
            return '0'
        while n != 0:
            rem = n % -2
            n = n // -2
            if rem < 0:
                rem += 2
                n += 1
            ret.append(rem)

        return ''.join([str(x) for x in ret[::-1]])
            
            
        
