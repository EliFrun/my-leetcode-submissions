class Solution:
    def binaryGap(self, n: int) -> int:
        ret = 0
        cnt = -50
        while n:
            if n & 1:
                ret = max(ret, cnt + 1)
                cnt = 0
            else:
                cnt += 1
            n >>= 1
        return ret
        
