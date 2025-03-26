class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        nums = sorted([x for x in nums if x <= target])
        n = len(nums)
        dp = [-math.inf] * (target+1)
        dp[0] = 0

        for num in nums:
            for new_sum in range(target, num-1, -1):
                dp[new_sum] = max(dp[new_sum], dp[new_sum-num]+1)
        
        return dp[-1] if dp[-1]!=-math.inf else -1
