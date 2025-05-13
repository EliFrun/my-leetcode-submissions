class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = 0
        ret = []
        for num in nums:
            n ^= num

            ret.append(~n & (2 ** maximumBit - 1))

        return ret[::-1]
        
