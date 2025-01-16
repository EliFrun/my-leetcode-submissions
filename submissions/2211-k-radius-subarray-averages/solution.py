class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ret = [-1] * len(nums)
        if k > len(nums) // 2:
            return ret
        s = 0
        for i, v in enumerate(nums):
            if i < 2 * k:
                s += v
                continue
            
            s += v
            ret[i - k] = s // (2 * k + 1)
            s -= nums[i - 2 * k]

        return ret
