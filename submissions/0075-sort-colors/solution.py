class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, one, two = 0, 0, 0
        for i in nums:
            if i == 0:
                zero += 1
            if i == 1:
                one += 1
            if i == 2:
                two += 2
                
        index = 0    
        for i in range(zero):
            nums[i] = 0
            
        for i in range(zero, zero + one):
            nums[i] = 1
            
        for i in range(zero + one, len(nums)):
            nums[i] = 2
