class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        below = 0
        above = sum(nums)
        ret = []
        for i, v in enumerate(nums):
            ret.append(v * i - below + above - v * (len(nums) - i))
            below += v
            above -= v
            
        return ret
            
        
