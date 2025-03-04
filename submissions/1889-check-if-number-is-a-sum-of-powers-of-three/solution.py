class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        k = int(log(n, 3))
        while n > 0:
            if n // (int(3 ** k)) > 1:
                return False
            n %= int(3 ** k)
            k -= 1

        return True

        
