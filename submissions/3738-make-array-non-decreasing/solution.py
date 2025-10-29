class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        curr = nums[0]
        ret = 0
        for v in nums:
            if v < curr:
                continue
            ret += 1
            if v > curr:
                curr = v
        return ret
        
