class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = tuple(points[0])
        x2, y2 = tuple(points[1])
        x3, y3 = tuple(points[2])
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) != 0
