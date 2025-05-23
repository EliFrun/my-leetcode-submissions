class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[0] * (minProfit + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(n - g, -1, -1):
                for j in range(minProfit, -1, -1):
                    dp[i + g][min(minProfit, j + p)] += dp[i][j]

        return sum(dp[i][-1] for i in range(len(dp))) % 1_000_000_007
