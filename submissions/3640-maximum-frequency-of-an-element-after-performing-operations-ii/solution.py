class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = SortedList(nums)

        ret = 0
        for num in nums:
            for v in [num - k, num, num + k]:
                c = nums.bisect_right(v) - nums.bisect_left(v)
                width = nums.bisect_right(v + k) - nums.bisect_left(v - k) - c
                ret = max(ret, c + min(numOperations, width))
        return ret
        
