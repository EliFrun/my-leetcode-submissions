class Solution:
    def countOrders(self, n: int) -> int:
        def fact(n):
            if n == 1:
                return n
            return n * fact(n - 1)
        
        return fact(2 * n) // 2 ** n % 1_000_000_007
        
