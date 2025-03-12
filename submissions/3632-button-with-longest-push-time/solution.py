class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        ret = events[0][0]
        m = events[0][1]
        for i in range(len(events) - 1):
            if events[i + 1][1] - events[i][1] > m:
                m = events[i + 1][1] - events[i][1]
                ret = events[i + 1][0]
            elif events[i + 1][1] - events[i][1] == m:
                ret = min(ret, events[i + 1][0])
        return ret
