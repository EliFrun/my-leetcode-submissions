class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if k == 0:
            return len(set(nums))
        s = SortedList(nums)
        ret = 0
        i = 0
        while i < len(s):
            v = s[i]
            i = s.bisect_right(v + k)
            if i < len(s) and s[i] == v + k:
                i += 1
            ret += 1

        return ret
        
