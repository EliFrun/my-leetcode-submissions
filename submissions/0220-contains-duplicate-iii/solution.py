class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        a = sorted(list(enumerate(nums)), key=lambda x: x[1])

        curr = [a[0]]
        indexes = SortedList([a[0][0]])
        i = 1
        while i < len(a):
            if a[i][1] > curr[0][1] + valueDiff:
                while curr and curr[0][1] + valueDiff < a[i][1]:
                    idx, v = curr.pop(0)
                    indexes.remove(idx)
            
            idx = indexes.bisect_left(a[i][0])
            comps = [max(idx - 1, 0), min(idx, len(indexes) - 1), min(idx + 1, len(indexes) - 1)]
            for comp in comps:
                if indexes and abs(indexes[comp] - a[i][0]) <= indexDiff:
                    return True
            curr.append(a[i])
            indexes.add(a[i][0])
            i += 1

        return False


        
