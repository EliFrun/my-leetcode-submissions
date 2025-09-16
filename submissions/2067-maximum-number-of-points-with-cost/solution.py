class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        curr = points[0]
        
        for i in range(1, len(points)):
            best_add = [0] * len(curr)
            right = SortedList([x - j for j, x in enumerate(curr)])
            for j in range(len(curr)):
                best_add[j] = right[-1] + j
                right.remove(curr[j] - j)
            
            left = SortedList([x + j for j, x in enumerate(curr)])
            for j in range(len(curr) - 1, -1, -1):
                best_add[j] = max(best_add[j], left[-1] - j)
                left.remove(curr[j] + j)


            curr = [points[i][j] + best_add[j] for j in range(len(curr))]
        
        
        return max(curr)

        
