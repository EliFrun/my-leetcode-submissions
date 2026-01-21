class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ret = []
        for num in nums:
            if num == 2:
                ret.append(-1)
                continue
            v = 1
            while num & v:
                v <<= 1
            v >>= 1
            ret.append(num ^ v)
        return ret
        
