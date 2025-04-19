class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        a = SortedList(nums)
        ret = 0
        for i,v in enumerate(a):
            left = max(i + 1, a.bisect_left(lower - v))
            right = min(len(nums), a.bisect_right(upper - v))
            ret += max(0, right - left)

        return ret
