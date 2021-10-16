class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dis = 100000
        ret = -1
        for index, lis in enumerate(points):
            i, j = lis[0], lis[1]
            if i != x and j != y:
                continue
            else:
                a = abs(i - x) + abs(j - y)
                if  a < dis:
                    dis = a
                    ret = index
                    
        return ret
                
        
