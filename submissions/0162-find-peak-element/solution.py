class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
            
        return i
