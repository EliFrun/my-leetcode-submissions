class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        i = 0
        while num1 > 0:
            if bin(num1).count('1') <= i <= num1:
                return i
            num1 -= num2
            i += 1
        return -1
        
