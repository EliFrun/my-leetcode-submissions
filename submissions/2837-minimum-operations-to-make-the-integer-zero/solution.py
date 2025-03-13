class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(61):
            #print(bin(num1 - i * num2), i)
            if bin(num1 - i * num2).count('1') <= i <= num1 - i * num2:
                return i

        return -1
        
