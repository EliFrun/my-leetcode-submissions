class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        v = 0
        for num in nums:
            v ^= num

        if v != 0:
            return len(nums)

        if max(nums) != 0:
            return len(nums) - 1
        return 0
        
