class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @cache
        def solve(i):
            if i >= len(nums):
                return True 
            if i == len(nums) - 1:
                return False
            ret = False
            if nums[i] == nums[i + 1]:
                ret = ret or solve(i + 2)

            if ret:
                return True
            
            if i < len(nums) - 2:
                if nums[i] + 1 == nums[i + 1] and nums[i + 1] + 1 == nums[i + 2]:
                    ret = ret or solve(i + 3)
                elif nums[i] == nums[i + 1] == nums[i + 2]:
                    ret = ret or solve(i + 3)
            return ret

        return solve(0)

        
