class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return (nums.sort() == None) and all(nums[i] == i + 1 for i in range(0, len(nums) - 1)) and nums[-1] == len(nums) - 1
        
