class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        @cache
        def solve(i, holding):
            if i == len(prices):
                return 0
            return max(solve(i + 1, True), solve(i + 1, False) + prices[i] - fee) if holding else max(solve(i + 1, False), solve(i + 1, True) - prices[i])

        return solve(0, False)

        
