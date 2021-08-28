class Solution:
    def findMin(self, nums: List[int]) -> int:
        bottom, top = 0, len(nums) - 1
        while top - bottom > 1 and nums[bottom] > nums[top]:
            middle = (bottom + top)//2
            if nums[middle] > nums[bottom]:
                bottom = middle
            else:
                top = middle
        
        first_index = top if nums[top] < nums[bottom] else bottom
        last_index = bottom if nums[top] < nums[bottom] else top
        
        return nums[first_index]
