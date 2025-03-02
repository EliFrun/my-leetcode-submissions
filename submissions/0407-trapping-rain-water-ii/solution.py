class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap[0])
        n = len(heightMap)
        h = []
        visited = set()
        for i in range(1, m - 1):
            h.append((heightMap[0][i], (0, i)))
            visited.add((0,i))

        for i in range(1, m - 1):
            h.append((heightMap[n - 1][i], (n - 1, i)))
            visited.add((n - 1,i))

        for i in range(1, n - 1):
            h.append((heightMap[i][0], (i, 0)))
            visited.add((i, 0))

        for i in range(1, n - 1):
            h.append((heightMap[i][m - 1], (i, m - 1)))
            visited.add((i, m - 1))

        visited.add((0,0))
        visited.add((0, m - 1))
        visited.add((n - 1,0))
        visited.add((n - 1, m - 1))

        heapq.heapify(h)
        ret = 0
        fill = [[0] * m for _ in range(n)]
        while len(visited) < m * n:
            height, (x, y) = heapq.heappop(h)
            dirs = [0,1,0,-1,0]
            for i in range(4):
                dx = dirs[i]
                dy = dirs[i + 1]
                if x + dx < 0 or x + dx >= n:
                    continue
                if y + dy < 0 or y + dy >= m:
                    continue

                if (x + dx, y + dy) in visited:
                    continue

                fill[x + dx][y + dy] = max(0, height - heightMap[x + dx][y + dy])
                ret += fill[x + dx][y + dy]
                visited.add((x + dx, y + dy))
                heapq.heappush(h, (max(heightMap[x + dx][y + dy], height), (x + dx, y + dy)))

        #print(*fill, sep='\n')
        return ret
            
