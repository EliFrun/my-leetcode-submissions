class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
    
        val = int(dividend/divisor)
        if abs(val) < 2**31:
            pass
        else:
            val = int(2**31 * (int(val)/ abs(int(val))))
            if val > 0:
                val -= 1
        return val
        
