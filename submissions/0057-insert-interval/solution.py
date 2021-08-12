class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        i = 1
        current_interval = intervals[0]
        ret = []
        while i < len(intervals):
            if intervals[i][0] <= current_interval[1]:
                current_interval[1] = max(intervals[i][1], current_interval[1])
            else:
                ret.append(current_interval)
                current_interval = intervals[i]
                
            i += 1
        
        ret.append(current_interval)
        
        return ret
