class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ret = 0
        slopes = defaultdict(lambda: set())
        for i, a in enumerate(points):
            for j , b in enumerate(points[i + 1:]):
                m = (b[1] - a[1]) / (b[0] - a[0]) if b[0] - a[0] != 0 else float('inf')
                y_int = b[1] - m * b[0] if b[0] - a[0] != 0 else b[0]
                slopes[m, y_int].add(tuple(a))
                slopes[m, y_int].add(tuple(b))

        
        return max(len(x) for x in list(slopes.values())) if slopes else len(points)
                    
        
        
