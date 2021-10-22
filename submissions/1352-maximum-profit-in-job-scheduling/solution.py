class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        cache = [-1] * len(startTime)
        
        def findBestAfterEnd(end, idx):
            nonlocal jobs
            for i in range(idx, len(jobs)):
                if jobs[i][0] >= end:
                    return i
                
            return len(jobs)
        
        def findOptimal(idx):
            nonlocal jobs
            nonlocal cache
            if idx >= len(jobs):
                return 0
            if cache[idx] > 0:
                return cache[idx]
            
            including_curr = jobs[idx][2] + findOptimal(findBestAfterEnd(jobs[idx][1], idx))
            without_curr = findOptimal(idx + 1)
            
            cache[idx] = max(including_curr, without_curr)
            return cache[idx]
        
        return findOptimal(0)
            
            
            
