class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = n * (n + 1)
        sumOdd = sumEven - n

        def gcd(x,y):
            if y == 0:
                return x
            return gcd(y, x % y)
        return gcd(sumEven, sumOdd)


        
