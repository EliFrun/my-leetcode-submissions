class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = SortedList(nums)
        ret = [0] * len(nums)
        for i, v in enumerate(nums):
            ret[i] = s.bisect_left(v)

        return ret
        
