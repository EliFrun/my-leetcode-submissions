class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if nums[0] == target else [-1, -1]
        if nums[0] > target:
            return [-1, -1]
        if nums[-1] < target:
            return [-1, -1]
        
        
        
        
        lower = upper = len(nums)//2
        
        step_size = len(nums)//4
        while step_size > 0:
                lower = lower - step_size if nums[lower] > target else lower + step_size
                step_size //= 2
                
        upper = lower

        if nums[lower] > target:
            while lower > 0 and nums[lower] >= target and not (nums[lower] == target and nums[lower - 1] != target):
                if nums[lower] > target and nums[lower - 1] < target:
                    return [-1, -1]
                lower -= 1
        elif nums[lower] < target:
            while lower < len(nums) - 1 and nums[lower] < target:
                print(lower)
                if nums[lower] < target and nums[lower + 1] > target:
                    return [-1, -1]
                lower += 1
        elif nums[lower] == target:
            while lower > 0 and nums[lower - 1] == target:
                lower -= 1
                
        if nums[upper] > target:
            while upper > 0 and nums[upper] > target:
                upper -= 1
        elif nums[upper] < target:
            while upper < len(nums) - 1 and nums[upper] <= target and not (nums[upper] == target and nums[upper + 1] != target):
                upper += 1
        elif nums[upper] == target:
            while upper < len(nums) - 1 and nums[upper + 1] == target:
                upper += 1
        
                

            
        return [lower, upper]
            
