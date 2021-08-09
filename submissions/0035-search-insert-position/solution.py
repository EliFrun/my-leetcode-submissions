class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 0 if target <= nums[0] else 1
        
        
        upper, lower = len(nums) - 1, 0
        while upper - lower > 1:
            middle = (upper + lower) // 2
            if target < nums[middle]:
                upper = middle
            else:
                lower = middle


        if nums[upper] == target:
            return upper
        if nums[lower] == target:
            return lower
        
        if target < nums[lower]:
            return lower
        elif target > nums[lower] and target < nums[upper]:
            return lower + 1
        else:
            return upper + 1
