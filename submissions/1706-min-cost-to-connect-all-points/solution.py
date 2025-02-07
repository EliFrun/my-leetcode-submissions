class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        ret = 0
        h = [(0, 0)]

        while len(visited) < len(points):
            cost, curr = heappop(h)
            if curr in visited:
                continue

            visited.add(curr)
            ret += cost
            for i in range(len(points)):
                if i in visited:
                    continue
                d = abs(points[curr][0] - points[i][0]) + abs(points[curr][1] - points[i][1])
                heappush(h, (d, i))
        return ret
                
        
