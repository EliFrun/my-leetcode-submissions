class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        l, r = (-1,-1)
        ret = 0
        for x,y in intervals:
            if l <= x and y <= r:
                continue
            ret += 1
            l, r = [x,y]
        return ret

        
