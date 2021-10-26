class Solution:
    def countOrders(self, n: int) -> int:
        if n == 1:
            return 1
        mod = 1_000_000_007
        return ((n * (2 * n - 1)) % mod) * (self.countOrders(n - 1) % mod) % mod
        
