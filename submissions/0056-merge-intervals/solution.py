class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ret = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= ret[-1][1]:
                ret[-1][1] = max(ret[-1][1], interval[1])
            else:
                ret.append(interval)
                
        return ret
