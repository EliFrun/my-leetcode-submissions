class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        right = points[0][1]
        ret = 1
        for l,r in points[1:]:
            if l > right:
                ret += 1
                right = max(r, right)
            else:
                right = min(r, right)

        return ret
        
