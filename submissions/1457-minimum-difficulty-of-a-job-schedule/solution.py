class Solution:
    def minDifficulty(self, jobs: List[int], d: int) -> int:
        if d > len(jobs):
            return -1
        @functools.cache
        def solve(i, d_left):
            if d_left == 1:
                return max(jobs[i:])
            ret = 1_000_000
            m = jobs[i]
            for j in range(i + 1, len(jobs) - d_left + 2):
                ret = min(ret, m + solve(j, d_left - 1))
                m = max(m, jobs[j])

            return ret

        return solve(0, d)
        
