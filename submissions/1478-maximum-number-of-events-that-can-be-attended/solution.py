class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        h = []
        heapify(events)
        ret = 0
        for i in range(1, max([x[1] for x in events]) + 1):
            while events and events[0][0] == i:
                s, e = heappop(events)
                heappush(h, e)
            while h and h[0] < i:
                heappop(h)
            if h:
                heappop(h)
                ret += 1

        return ret
        
