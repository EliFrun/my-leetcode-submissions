class Solution:
    def maxRectangleArea(self, points: List[List[int]]) -> int:
        points.sort()
        best = -1
        for i in range(len(points) - 1):
            if points[i][0] != points[i + 1][0]:
                continue
            lower, upper = points[i][1], points[i + 1][1]
            for j in range(i + 2, len(points) - 1):
                if lower < points[j][1] < upper:
                    break
                if points[j][1] in (lower, upper) and (points[j + 1][1] not in (lower, upper) or points[j + 1][0] != points[j][0]):
                    break
                elif points[j][1] == lower:
                    if points[j + 1][0] == points[j][0] and points[j + 1][1] == upper:
                        best = max(best, (upper - lower) * (points[j][0] - points[i][0]))

        return best

            
        
