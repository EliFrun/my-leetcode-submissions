class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        window = defaultdict(int)
        ret = 0
        discarded = set()
        for i, v in enumerate(arrivals):
            if i >= w and i - w not in discarded:
                window[arrivals[i - w]] -= 1
            
            if window[v] == m:
                discarded.add(i)
                ret += 1
            else:
                window[v] += 1
        return ret
                
        
