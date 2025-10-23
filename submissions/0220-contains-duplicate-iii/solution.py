class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        l = SortedList()
        for i,v in enumerate(nums):
            if l:
                idx = l.bisect_left(v)
                if idx - 1 >= 0 and abs(l[idx - 1] - v) <= valueDiff:
                    return True
                if idx < len(l) and abs(l[idx] - v) <= valueDiff:
                    return True
                if idx + 1 < len(l) and abs(l[idx + 1] - v) <= valueDiff:
                    return True
            l.add(v)
            if i >= indexDiff: (l.remove(nums[i - indexDiff]))
        return False


        
