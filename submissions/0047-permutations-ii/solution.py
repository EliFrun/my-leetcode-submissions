class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        if not nums:
            return []
        ret = []
        current = {}
        for i in nums:
            if i in current:
                continue
            current[i] = 1
            cp = nums.copy()
            cp.remove(i)
            for j in self.permuteUnique(cp):
                ret.append([i] + j)
                
        return ret
        
