class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        M = 1_000_000_007
        dp = [0] * len(nums)
        left = 0
        s = SortedList()
        prefix = 0
        for i, num in enumerate(nums):
            s.add(num)
            while s[-1] - s[0] > k:
                s.remove(nums[left])
                prefix = (prefix - dp[left] + M) % M
                left += 1

            if left == 0:
                dp[i] += 1
            else:
                dp[i] = (dp[i] + dp[left - 1]) % M
            dp[i] = (dp[i] + prefix) % M
            
            prefix = (prefix + dp[i]) % M

        return dp[-1] % M

        
