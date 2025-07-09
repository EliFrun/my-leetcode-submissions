class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        events = sorted(list(zip(startTime, endTime)))
        curr = 0
        diffs = []
        for s, e in events:
            diffs.append(s - curr)
            curr = e
        diffs.append(eventTime - curr)
        size = sum(diffs[:k + 1])
        ret = size
        i = 0
        for diff in diffs[k + 1:]:
            size += diff
            size -= diffs[i]
            i += 1
            ret = max(ret, size)
        return ret
