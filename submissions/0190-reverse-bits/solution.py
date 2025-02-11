class Solution:
    def reverseBits(self, n: int) -> int:
        ret = ''
        for i in range(32):
            ret += str(n % 2)
            n = n // 2

        r = 0
        for i in range(1, 33):
            r += int(ret[i - 1]) * 2 ** (32 - i)

        return r


        
