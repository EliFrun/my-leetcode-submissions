class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        lower, upper = 1,1
        
        while upper * upper < x:
            upper *= 2
            
            
        while upper - lower > 1:
            mid = (lower + upper) // 2
            if mid * mid < x:
                lower = mid
            else:
                upper = mid
                
        return lower if upper * upper > x else upper
