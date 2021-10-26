class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        employees = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        
        q = []
        best = 0
        curr_sum = 0
        for s, e in employees:
            if len(q) < k:
                curr_sum += s
                heappush(q, s)
            else:
                if s > q[0]:
                    curr_sum = curr_sum - heappushpop(q, s) + s
                    
            best = max(best, curr_sum * e)
                
        return best % 1_000_000_007
                       
                        
            
        
