class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        return ((n) * (2 * n - 1) * self.countOrders(n - 1)) % 1_000_000_007
        
