class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        h = []  
        ret = 0
        i = 0
        while i < len(apples) or h:
            if i < len(apples):
                a, d = apples[i], days[i]
                heapq.heappush(h, [i + d - 1, -a])
            
            while h and h[0][0] < i:
                heapq.heappop(h)
            if h:
                ret += 1
                h[0][1] += 1
                if h[0][1] == 0:
                    heapq.heappop(h)
            i += 1

        return ret
    
        
