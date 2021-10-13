class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mix = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        
        ret = 0
        q = []
        curr_sum = 0
        for s, e in mix:
            if len(q) < k:
                curr_sum += s
                heappush(q, s)
            else:
                if s > q[0]:
                    curr_sum += s - heappushpop(q, s)    
                
            ret = max(ret, curr_sum * e)
                
        return ret % 1_000_000_007
                
            
        
