class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        l = [bottomLeft[i] + topRight[i] for i in range(len(bottomLeft))]
        l.sort()
        print(l)
        ret = 0
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                s1 = l[i]
                s2 = l[j]
                
                if s2[1] >= s1[3]:
                    continue 

                if s2[0] >= s1[2]:
                    break

                # s1 encompasses s2
                if s1[0] <= s2[0] and s1[2] >= s2[2] and s1[1] <= s2[1] and s1[3] >= s2[3]:
                    ret = max(ret, min(s2[2] - s2[0], s2[3] - s2[1]))
                    continue

                if s2[0] <= s1[0] and s2[2] >= s1[2] and s2[1] <= s1[1] and s2[3] >= s1[3]:
                    ret = max(ret, min(s1[2] - s1[0], s1[3] - s1[1]))
                    continue

                bl_x = max(s1[0], s2[0])
                bl_y = max(s1[1], s2[1])

                tr_x = min(s1[2], s2[2])
                tr_y = min(s1[3], s2[3])

                dx = max(0, tr_x - bl_x)
                dy = max(0, tr_y - bl_y)
                ret = max(ret, min(dx, dy))
        return ret * ret
        
