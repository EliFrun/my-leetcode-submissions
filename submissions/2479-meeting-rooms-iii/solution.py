class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        h = [(0, i) for i in range(n)]
        heapify(h)
        res = defaultdict(int)
        for s, e in sorted(meetings):
            while h[0][0] < s:
                _, i = heappop(h)
                heappush(h, (s, i))
            t, i = heappop(h)
            res[i] += 1
            if t >= s:
                e = t + (e - s)
            heappush(h, (e, i))


        return -max([(v,-k) for k,v in res.items()])[1]
            
            

        
