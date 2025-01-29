class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ret = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                ret.append(nums[i])
        
        return ret
        
