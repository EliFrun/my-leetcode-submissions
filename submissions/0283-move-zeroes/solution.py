class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = []
        
        count = 0
        
        for i in nums:
            if i == 0:
                count += 1
            else:
                x.append(i)
                
        for i, val in enumerate(x + [0] * count):
            nums[i] = val
