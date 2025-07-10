class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        diffs = []
        prev = 0
        for s, e in zip(startTime, endTime):
            diffs.append(s - prev)
            prev = e

        diffs.append(eventTime - prev)
        
        best = max([diffs[i] + diffs[i + 1] for i in range(len(diffs) - 1)])
        left = SortedList()
        right = SortedList(diffs[1:])
        for i in range(len(startTime)):
            right.remove(diffs[i + 1])
            event_time = endTime[i] -  startTime[i]
            if left.bisect_left(event_time) < len(left) or right.bisect_left(event_time) < len(right):
                best = max(best, diffs[i] + diffs[i + 1] + event_time)
            left.add(diffs[i])
        return best

