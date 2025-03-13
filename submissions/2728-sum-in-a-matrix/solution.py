class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for i in range(len(nums)):
            nums[i].sort()

        ret = 0
        for j in range(len(nums[0])):
            ret += max([nums[i][j] for i in range(len(nums))])

        return ret
             
        
