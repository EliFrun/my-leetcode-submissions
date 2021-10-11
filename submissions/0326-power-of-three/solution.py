class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        return (n / 3).is_integer() and self.isPowerOfThree(n / 3)
