class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        s = SortedList()
        for i, q in enumerate(queries):
            s.add((q, i))

        intervals.sort(key=lambda x: x[1] - x[0])

        ret = [-1] * len(queries)
        for l, r in intervals:
            idx_left = s.bisect_left((l, -1))
            idx_right = s.bisect_right((r, float('inf')))

            for i in range(idx_right - 1, idx_left - 1, -1):
                q, j = s.pop(i)
                ret[j] = r - l + 1
        return ret

        
