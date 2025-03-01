class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = 2 * nums[i]
                nums[i + 1] = 0

        ret = [0] * len(nums)
        i = 0
        for n in nums:
            if n != 0:
                ret[i] = n
                i += 1
        
        return ret
        
            
        

        
