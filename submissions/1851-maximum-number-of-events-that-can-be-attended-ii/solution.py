class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = SortedList(events)
        nxt_indexes = [0] * len(events)
        for i in range(len(events)):
            nxt_indexes[i] = events.bisect_left([events[i][1] + 1, 0, 0])

        @cache
        def solve(i, left):
            if left == 0:
                return 0
            if i >= len(events):
                return 0
            
            return max(solve(i + 1, left), solve(nxt_indexes[i], left - 1) + events[i][2])
        return solve(0, k)
        
