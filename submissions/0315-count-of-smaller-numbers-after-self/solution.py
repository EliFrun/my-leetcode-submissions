class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = SortedList()
        ret = [0] * len(nums)
        for i, n in enumerate(nums[::-1]):
            less = l.bisect_left(n)
            ret[-i - 1] = less
            l.add(n)

        return ret
        
