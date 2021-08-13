class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(0, len(nums) + 1):
            ret.extend(self.helper(nums, 0, i))
            
        return ret
    

    def helper(self, nums, lower, k):
        if k == 0:
            return [[]]
        if k == 1:
            return [[x] for x in nums[lower:]]
        ret = []
        index = lower
        for i in nums[lower:]:
            ret.extend([i] + x for x in self.helper(nums, index + 1, k - 1))
            index += 1
                
        return ret
