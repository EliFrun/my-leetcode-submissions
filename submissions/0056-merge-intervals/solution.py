class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr = intervals[0]
        ret = []
        for l, r in intervals[1:]:
            if l <= curr[1]:
                curr[1] = max(curr[1], r)
            else:
                ret.append(curr)
                curr = [l,r]

        ret.append(curr)
        return ret
        
