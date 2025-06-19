class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        @cache
        def cnt(v):
            ret = 0
            for i in range(1, m + 1):
                if v // i == 0:
                    break
                ret += min(n, v // i)
            return ret

        lower = 1
        upper = n * m
        ret = -1
        while lower < upper:
            middle = (upper + lower) // 2
            if cnt(middle) < k:
                lower = middle + 1
            else:
                upper = middle

        return lower

        
