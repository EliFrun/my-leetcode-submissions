class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        cache = [-1 for _ in range(len(jobs))]
    
        def nextJob(idx, endtime):
            nonlocal jobs
            for i in range(idx, len(jobs)):
                if jobs[i][0] >= endtime:
                    return i
                
            return len(jobs)
        
        def bestSchedule(idx):
            nonlocal jobs
            nonlocal cache
            if idx >= len(jobs):
                return 0
            if cache[idx] >= 0:
                return cache[idx]
            
            with_curr = jobs[idx][2] + bestSchedule(nextJob(idx, jobs[idx][1]))
            without_curr = bestSchedule(idx + 1)
            cache[idx] = max(with_curr, without_curr)
            return cache[idx]
        
        return bestSchedule(0)
            
            
            
