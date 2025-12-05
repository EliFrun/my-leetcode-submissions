class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods)
        dp = [0] * (sum(rods) + 1)
        dp[s] = s
        for rod in rods:
            for i in range(len(dp) - rod):
                if i + 2 * rod < len(dp):
                    dp[i] = max(dp[i + 2 * rod] - rod, dp[i])
                dp[i] = max(dp[i + rod] - rod, dp[i])
        return dp[0]
            
        
