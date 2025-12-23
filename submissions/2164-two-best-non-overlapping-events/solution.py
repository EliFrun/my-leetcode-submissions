class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        best = [0] * len(events)
        best[-1] = events[-1][2]
        for i in range(len(events) - 2, -1, -1):
            best[i] = max(best[i + 1], events[i][2])
        ret = 0
        for s,e,v in events:
            idx = bisect_left(events, [e + 1, -1, -1])
            if idx < len(best):
                v += best[idx]
            ret = max(ret, v)
        return ret
