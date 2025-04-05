class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ret = 0
        for i in range(2 ** len(nums)):
            v = 0
            for j in range(len(nums)):
                if i >> j & 1:
                    v ^= nums[j]

            ret += v

        return ret
