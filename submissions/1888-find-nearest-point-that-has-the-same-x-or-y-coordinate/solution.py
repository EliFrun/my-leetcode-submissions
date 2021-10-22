class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ret = -1
        closest_distance = 1_000_000
        for i, (a, b) in enumerate(points):
            if a == x:
                dis = abs(y - b)
                if dis < closest_distance:
                    closest_distance = dis
                    ret = i
            elif b == y:
                dis = abs(x - a)
                if dis < closest_distance:
                    closest_distance = dis
                    ret = i
                    
        return ret
        
                
        
