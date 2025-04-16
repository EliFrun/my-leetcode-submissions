class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                continue
            j = i
            while j + 1 < len(nums) and nums[j + 1] != 0:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
                j += 1
        
        
