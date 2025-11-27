class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)
        cnt = 0
        curr = 0
        for i, num in enumerate(nums):
            cnt += 1
            curr += num
            if cnt > k:
                curr -= nums[i - k]
                cnt -= 1
            if cnt == k:
                dp[i] = curr
            if i >= k:
                dp[i] = max(dp[i - k] + curr, curr)
        
        return max(dp[k - 1:])
            
        
