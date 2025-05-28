class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        s = sum(rods)
        dp = [0] * (s + 1)
        dp[s] = s

        for rod in rods:
            for i in range(len(dp)):
                if i - rod >= 0:
                    dp[i - rod] = max(dp[i - rod], dp[i] - rod)
                if i - 2 * rod >= 0:
                    dp[i - 2 * rod] = max(dp[i - 2 * rod], dp[i] - rod)
            
    
        return dp[0]
        
