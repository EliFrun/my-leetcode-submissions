class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        schedules = sorted(zip(startTime, endTime, profit), key=lambda x: (x[0], x[1]))
        cache = [-1] * len(endTime)
        # list is sorted so this could be O(logn)
        def indexAfterEnd(end, idx):
            nonlocal schedules
            i, j = idx, len(schedules)
            while i + 1 < j:
                mid = (i+j)//2
                if schedules[mid][0] >= end:
                    j = mid
                else:
                    i = mid
            
            if min(i, j) >= len(schedules):
                return min(i, j)
            return i if schedules[i][0] >= end else j
            
        
        def findOptimal(idx):
            nonlocal schedules
            if idx >= len(schedules):
                return 0

            nonlocal cache
            if cache[idx] >= 0:
                return cache[idx]
            
            with_curr = schedules[idx][2] + findOptimal(indexAfterEnd(schedules[idx][1], idx))
            cache[idx] = max(with_curr, findOptimal(idx + 1))
            return cache[idx]
        
        return findOptimal(0)
            
            
            
