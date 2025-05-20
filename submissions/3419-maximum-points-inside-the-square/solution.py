class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ret = float('inf')
        d = defaultdict(SortedList)
        for (x,y), c in zip(points, s):
            d[c].add(max(abs(x), abs(y)))
        
        for k in d.keys():
            if len(d[k]) > 1:
                ret = min(d[k][1] - 1, ret)

        return len([x for x in d.keys() if d[x][0] <= ret])
