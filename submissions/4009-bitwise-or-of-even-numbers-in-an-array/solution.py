class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ret = 0
        for x in nums:
            if x & 1:
                continue
            ret |= x
        return ret
        
