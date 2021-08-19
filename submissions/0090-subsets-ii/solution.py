class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(0, len(nums) + 1):
            ret.extend(self.helper(nums, 0, i))
            
        return ret
    

    def helper(self, nums, lower, k):
        if k == 0:
            return [[]]
        if k == 1:
            return [[x] for x in list(dict.fromkeys(nums[lower:]))]
        ret = []
        index = lower
        previous_num = -11
        for i in nums[lower:]:
            if i == previous_num:
                index += 1
                continue
            previous_num = i
            ret.extend([i] + x for x in self.helper(nums, index + 1, k - 1))
            index += 1
                
        return ret
