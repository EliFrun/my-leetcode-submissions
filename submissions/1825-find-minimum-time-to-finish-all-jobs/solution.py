class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)

        best = float("Inf")
        times = [0] * k
        def solve(i):
            
            nonlocal best
            if i == len(jobs):
                best = max(times)
                return
            for j in range(k):
                if j > 0 and times[j] == times[j - 1]:
                    continue
                times[j] += jobs[i]
                if max(times) < best:
                    solve(i + 1)
                times[j] -= jobs[i] 

        solve(0)
        return best
        
        
