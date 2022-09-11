class Solution:
    def binaryGap(self, n: int) -> int:
        val = bin(n)[2:]
        if val.count('1') <= 1:
            return 0
        val = val.strip('0')
        gaps = val.split('1')
        return max([len(x) + 1 for x in gaps])
        
