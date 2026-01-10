class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        N = len(runningCosts)
        vals = SortedList()
        ret = 0
        right = 0
        prefix = 0
        for i in range(N):
            while right < N:
                vals.add(chargeTimes[right])
                prefix += runningCosts[right]
                right += 1
                if vals[-1] + (len(vals)) * prefix > budget:
                    break
                ret = max(ret, len(vals))
            
            vals.remove(chargeTimes[i])
            prefix -= runningCosts[i]

        return ret
        
