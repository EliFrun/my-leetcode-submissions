class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ret = [1] * n

        rem = k - n
        for i in range(len(ret) - 1, -1, -1):
            ret[i] = min(1 + rem, 26)
            rem -= 25
            if rem <= 0:
                break

        return ''.join([chr(ord('a') - 1 + i) for i in ret])

        
        
