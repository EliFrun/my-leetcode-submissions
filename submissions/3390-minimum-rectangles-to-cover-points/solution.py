class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(list(set([x[0] for x in points])))
        right = points[0] + w
        ret = 1
        for point in points:
            if point > right:
                right = point + w
                ret += 1

        return ret
            
        
