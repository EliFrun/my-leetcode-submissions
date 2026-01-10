class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        if angle == 360:
            return len(points)
        x,y = location

        lis = []
        free = 0
        for xx, yy in points:
            run = xx - x
            rise = yy - y
            hypot = sqrt(rise ** 2 + run ** 2)
            if hypot == 0:
                free += 1
                continue
            angle1 = degrees(acos(run/hypot))
            if rise < 0:
                angle1 = 360 - angle1
            lis.append(round(angle1, 12))

        lis.sort()
        if not lis:
            return free
        lis2 = [x - 360 for x in lis] + lis

        ret = 0
        left = len(lis)
        while left >= 0 and lis[0] - angle <= lis2[left]:
            left -= 1
        if left == 0:
            return len(points)
    
        
        for i in range(len(lis), len(lis2)):
            while (lis2[i] - angle) > lis2[left]:
                left += 1 
            ret = max(ret, i - left + 1)
            

        return free + ret
