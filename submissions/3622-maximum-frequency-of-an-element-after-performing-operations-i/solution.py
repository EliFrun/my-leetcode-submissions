class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums = SortedList(nums)
        ret = 0
        for num in range(min(nums), max(nums) + 1):
            cnt = nums.bisect_right(num) - nums.bisect_left(num)
            extra = nums.bisect_right(num + k) - nums.bisect_right(num) + nums.bisect_left(num) - nums.bisect_left(num - k)
            ret = max(ret, cnt + min(numOperations, extra))
        return ret
        
