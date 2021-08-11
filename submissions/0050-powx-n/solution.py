class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == -1:
            return 1/x
        if n == 0:
            return 1
        if n == 1:
            return x
        
        a = self.myPow(x, n // 2)
        b = self.myPow(x, n % 2)
        
        return a * a * b
