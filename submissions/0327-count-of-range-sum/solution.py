class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        p = 0
        s = SortedList([0])
        
        ret = 0
        for num in nums:
            p += num
            left, right = p - upper, p - lower
            ret += s.bisect_right(right) - s.bisect_left(left)
            s.add(p)

        return ret
        
