class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1)] * len(nums)
        for i in range(len(dp)):
            v = 1
            cnt = 1
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                if dp[j][0] + 1 > v:
                    v = dp[j][0] + 1
                    cnt = dp[j][1]
                elif dp[j][0] + 1 == v:
                    cnt += dp[j][1]
            dp[i] = (v, cnt)
        m = max(x for x,y in dp)
        return sum(y for x,y in dp if x == m)

