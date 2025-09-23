class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        ret = 0
        M = 1_000_000_007
        c = comb(m * n - 2, k - 2) % M

        for i in range(m):
            for j in range(n):
                mm = ((m - i - 1) * (m - i) // 2) * n
                nn = ((n - j - 1) * (n - j) // 2) * m
                v = mm + nn
                ret = (ret + v * c) % M

        return ret
        
