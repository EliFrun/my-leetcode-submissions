class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        left = 0
        ret = 0
        for v in nums:
            if v == 0:
                if left - s == 0:
                    ret += 2
                elif abs(left - s) == 1:
                    ret += 1
            s -= v
            left += v
        return ret
        
