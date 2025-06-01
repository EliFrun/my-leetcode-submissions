class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        @cache
        def solve(left, pp, i):
            if left < 0:
                return 0
            if i >= len(group):
                return 1 if pp == 0 else 0
            return (solve(left - group[i], max(0, pp - profit[i]), i + 1) + solve(left, pp, i + 1)) % 1_000_000_007

        return solve(n, minProfit, 0)
