class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        l = [0] * len(nums)
        for i, num in enumerate(nums):
            l[i] = sum(nums[max(0, i - num):i + 1])
        return sum(l)
        
