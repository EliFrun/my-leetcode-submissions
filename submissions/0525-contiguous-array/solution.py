class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        vals = [0]
        for num in nums:
            vals.append(vals[-1] + (1 if num == 1 else -1))

        d = {}
        for i, val in enumerate(vals):
            d[val] = i
        
        ret = 0
        for i, val in enumerate(vals):
            if val in d:
                ret = max(ret, abs(i - d[val]))


        return ret
                
        
        
