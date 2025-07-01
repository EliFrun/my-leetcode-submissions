class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = SortedList(list(range(n)))
        ret = []
        for start, end in queries:
            bottom_index = s.bisect_right(start)
            top_index = s.bisect_left(end)
            for i in range(top_index - 1, bottom_index - 1, -1):
                s.remove(s[i])

            ret.append(len(s) - 1)
        return ret
        
