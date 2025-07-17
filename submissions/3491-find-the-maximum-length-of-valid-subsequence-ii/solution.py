class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        nums = [x % k for x in nums]

        dp = [[0] * k for _ in range(k)]
        for num in nums:
            for v in range(k):
                dp[v][num] = dp[num][v] + 1

        return max([max(lis) for lis in dp])
        
