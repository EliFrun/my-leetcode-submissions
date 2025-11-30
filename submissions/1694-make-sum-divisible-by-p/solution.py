class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums) % p
        if s == 0:
            return 0

        c = 0
        d = { 0: -1 }
        ret = float('inf')
        for i, num in enumerate(nums):
            c = (c + num) % p
            if (c - s + p) % p in d:
                ret = min(ret, i - d[(c - s + p) % p])
            d[c] = i
        

        if ret >= len(nums):
            return -1
        return ret
