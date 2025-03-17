class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ret = [0] * 32
        for i in range(32):
            for num in nums:
                ret[- i - 1] += (num >> i) & 1


        r = 0
        for i in range(32):
            if ret[-i - 1] >= k:
                r |= (1) << i

        return r
