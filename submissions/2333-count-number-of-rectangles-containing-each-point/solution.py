class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rects = defaultdict(SortedList)
        for x,y in rectangles:
            rects[y].add(x)

        ret = []
        for x,y in points:
            v = 0
            for key in [k for k in rects.keys() if k >= y]:
                v += len(rects[key]) - rects[key].bisect_right(x - 1)

            ret.append(v)
        return ret


        
