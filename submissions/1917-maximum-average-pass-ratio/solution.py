class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        q = []
        for i in range(len(classes)):
            p, t = classes[i]
            heappush(q, ((p/t - (p + 1)/(t + 1)), i))
        
        while extraStudents > 0:
            _, i = heappop(q)
            classes[i][0] += 1
            classes[i][1] += 1
            p,t = classes[i]
            heappush(q, (p/t - (p + 1)/(t + 1), i))
            extraStudents -= 1

        return sum(p/t for p, t in classes) / len(classes)
