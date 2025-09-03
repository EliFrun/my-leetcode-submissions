class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        ret = 0
        for i in range(len(points)):
            x, y = points[i]
            min_y = -1e9 - 1
            for j in range(i + 1, len(points)):
                xx, yy = points[j]
                if yy > min_y and yy <= y:
                    ret += 1
                if yy <= y:
                    min_y = max(min_y, yy)

        return ret
        
