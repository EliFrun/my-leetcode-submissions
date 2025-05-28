class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        curr = 0
        ret = []
        for num in nums:
            s -= num
            ret.append(abs(curr - s))
            curr += num

        return ret
