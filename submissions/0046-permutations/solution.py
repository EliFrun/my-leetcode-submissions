class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if not nums:
            return []
        ret = []
        for i in nums:
            cp = nums.copy()
            cp.remove(i)
            for j in self.permute(cp):
                ret.append([i] + j)
                
        return ret
