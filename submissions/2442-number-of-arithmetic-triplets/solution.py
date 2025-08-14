class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        s = set(nums)
        ret = 0
        for num in s:
            if num + diff in s and num + 2 * diff in s:
                ret += 1

        return ret
        
