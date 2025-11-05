class Solution:
    def mySqrt(self, x: int) -> int:
        ret = 0
        left, right = 0, x
        while left <= right:
            middle = (left + right) // 2
            if middle * middle <= x:
                ret = middle
                left = middle + 1
            else:
                right = middle - 1
        return ret
        
