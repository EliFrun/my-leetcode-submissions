class Solution:
    def accountBalanceAfterPurchase(self, p: int) -> int:
        return 100 - ((p + 5) // 10) * 10
        
