class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [0] * (n + 1)
        dp[-1] = 1
        i = 1
        while i ** x <= n:
            for j in range(i ** x, n + 1):
                dp[j - i ** x] += dp[j]
            i += 1


        return dp[0] % 1_000_000_007
        
