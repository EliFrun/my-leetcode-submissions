class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        nums = sorted([(x, i) for i, x in enumerate(nums)], key=lambda x: x[0])
        
        while j > i:
            if nums[i][0] + nums[j][0] > target:
                j -= 1
            elif nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                return [nums[i][1], nums[j][1]]
                
