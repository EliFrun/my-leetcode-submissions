class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:]
        h = [(-nums[0], 0)]
        for i,v in enumerate(nums):
            if i == 0:
                continue
            m = 0
            while h[0][1] < i - k:
                heappop(h)
            dp[i] = max(dp[i], nums[i] - h[0][0])
            heappush(h, (-dp[i], i))

        return max(dp)


        
