class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1
        def solve(upper):
            ret = 0
            i = 0
            count = 0
            while i < len(bloomDay):
                if bloomDay[i] <= upper:
                    count += 1
                else:
                    ret += count // k
                    count = 0
                i += 1
            ret += count // k
            return ret

        opts = sorted(list(set(bloomDay)))
        left,right = 0, len(opts) - 1
        ret = -1
        while left <= right:
            middle = opts[(left + right) //2]
            if solve(middle) >= m:
                ret = middle
                right = (left + right) // 2 - 1
            else:
                left = (left + right) // 2 + 1
        
        return ret
        
