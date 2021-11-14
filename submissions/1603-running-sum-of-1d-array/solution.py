class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            ret.append(ret[-1] + i if ret else i)
            
        return ret
