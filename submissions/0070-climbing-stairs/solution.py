class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        a,b  = 1, 1
        for i in range(0, n):
            a, b = b, a + b
            
            
        return a
        
