class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        closest_dis = 10000000
        ret = -1
        for point in [(i, point) for i, point in enumerate(points) if point[0] == x or point[1] == y]:
            idx = point[0] 
            a, b = point[1]
            dis = abs(x - a) + abs(y - b)
            if dis < closest_dis:
                ret = idx
                closest_dis = dis
                
        return ret
        
                
        
