class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        ret = SortedList()
        for l, r in intervals:
            v = ret.bisect_right(r) - ret.bisect_left(l)
            if v >= 2:
                continue
            elif v == 1:
                while r in ret:
                    r -= 1
                ret.add(r)
            else:
                ret.add(r - 1)
                ret.add(r)
        return len(ret)
                    
        
