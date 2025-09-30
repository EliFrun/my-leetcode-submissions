class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ret = 0
        for i, num in enumerate(nums):
            ret = (ret + num * comb(len(nums) - 1, i)) % 10
        return ret
