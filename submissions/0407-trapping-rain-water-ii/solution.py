class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ret = 0
        q = []
        for i in range(1, len(heightMap) - 1):
            heappush(q, (heightMap[i][0], i, 0))
            heappush(q, (heightMap[i][len(heightMap[0]) - 1], i, len(heightMap[0]) - 1))

        for j in range(1, len(heightMap[0]) - 1):
            heappush(q, (heightMap[0][j], 0, j))
            heappush(q, (heightMap[len(heightMap) - 1][j], len(heightMap) - 1, j))

        visited = set([(x,y) for h, x, y in q])
        visited.update([
            (0,0),
            (0, len(heightMap[0]) - 1),
            (len(heightMap) - 1, 0),
            (len(heightMap) - 1, len(heightMap[0]) - 1)
        ])
        while q:
            h, x, y = heappop(q)
            visited.add((x,y))
            dirs = [0,1,0,-1,0]
            for i in range(4):
                dx, dy = dirs[i], dirs[i + 1]
                if not (0 <= x + dx < len(heightMap) and 0 <= y + dy < len(heightMap[0])):
                    continue
                if (x + dx, y + dy) in visited:
                    continue
                visited.add((x + dx, y + dy))
                ret += max(0, h - heightMap[x + dx][y + dy])
                heightMap[x + dx][y + dy] = max(h, heightMap[x + dx][y + dy])
                heappush(q, (heightMap[x + dx][y + dy], x + dx, y + dy))

        print(*heightMap, sep='\n')
        return ret

