class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_val = []
        for point in points:
            x_val.append(point[0])
            
        list.sort(x_val)
        
        max_dist = 0
        for i in range(len(x_val) - 1):
            max_dist = max(max_dist, x_val[i + 1] - x_val[i])
            
        return max_dist
