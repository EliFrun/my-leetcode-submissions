class Solution:
    def minimumBoxes(self, n: int) -> int:

        def arithmetic_series(v):
            ret = 0
            left, right = 0, v
            while left <= right:
                middle = (left + right) // 2
                if (middle * (middle + 1)) // 2 <= v:
                    ret = middle
                    left = middle + 1
                else:
                    right = middle - 1
            return ret

        @cache
        def solve(floor):
            if floor < 3:
                return floor
            v = arithmetic_series(floor)
            l = (v * (v - 1)) // 2
            diff = floor - (v * (v + 1)) // 2
            l += max(0, diff - 1)
            return floor + solve(l)


        ret = 0
        left, right = 0, n
        while left <= right:
            middle = (left + right) // 2
            if solve(middle) < n:
                left = middle + 1
            else:
                ret = middle
                right = middle - 1
        return ret

            
