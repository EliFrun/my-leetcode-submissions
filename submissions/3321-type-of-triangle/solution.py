class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[2] >= nums[1] + nums[0]:
            return 'none'
        
        if all(num == nums[-1] for num in nums):
            return 'equilateral'
        
        if nums[0] == nums[1] or nums[1] == nums[2]:
            return 'isosceles'
        
        return 'scalene'
