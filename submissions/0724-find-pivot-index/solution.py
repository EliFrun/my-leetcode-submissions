class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_left = [0] * (len(nums) + 1)
        for index, value in enumerate(nums):
            sum_left[index + 1] = sum_left[index] + value
            
            
        sum_right = [0] * (len(nums) + 1)
        for index, value in enumerate(nums[::-1]):
            sum_right[index + 1] = sum_right[index] + value            
            
        sum_right = sum_right[::-1]
        
        for i in range(len(nums)):
            if sum_left[i] == sum_right[i + 1]:
                return i
            
        return -1
            
        
