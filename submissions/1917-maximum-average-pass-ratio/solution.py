class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classes = [(
                -((x[0] + 1)/(x[1] + 1) - x[0]/x[1]),
                x[0],
                x[1]
            ) for x in classes]
        heapify(classes)
        while extraStudents:
            curr = heappop(classes)
            curr = (
                -((curr[1] + 2)/(curr[2] + 2) - (curr[1] + 1)/(curr[2] + 1)),
                curr[1] + 1,
                curr[2] + 1
            ) 
            heappush(classes, curr)
            extraStudents -= 1
        
        avg = 0
        for c in list(classes):
            avg += c[1]/c[2]
            
            
        return avg/len(classes)
            
        
        
