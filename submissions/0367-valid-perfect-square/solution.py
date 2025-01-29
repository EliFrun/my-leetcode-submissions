class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def cus_sqrt(x):
            n = x
            n1 = (1 / 2) * (x + x / n)
            while abs(n1 - n) > 0.0001:
                n = n1
                n1 = (0.5) * (n + x / n)

            return n1

        sq = int(cus_sqrt(num))
        return sq * sq == num
        
