class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        right = intervals[0][1]
        ret = 0
        for l,r in intervals[1:]:
            if l < right:
                ret += 1
            else:
                right = r

        return ret
            
        
