class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        r = defaultdict(SortedList)
        for x,y in rectangles:
            r[y - 1].add(x)

        keys = SortedList(r.keys())

        ret = []
        for x,y in points:
            cnt = 0
            for i in keys[keys.bisect_left(y - 1):]:
                cnt += len(r[i]) - r[i].bisect_left(x)

            ret.append(cnt)
        return ret
