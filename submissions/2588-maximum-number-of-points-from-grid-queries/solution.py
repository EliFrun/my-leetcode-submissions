class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        foo = sorted(queries)
        memo = {}
        count = 0
        pq = [(grid[0][0],(0,0))]
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for q in foo:
            while len(pq) > 0 and pq[0][0] < q:
                _, (i,j) = heapq.heappop(pq)
                if visited[i][j]:
                    continue
                visited[i][j] = True
                count += 1
                dirs = [0,1,0,-1,0]
                for k in range(4):
                    di, dj = dirs[k], dirs[k + 1]
                    if i + di < 0:
                        continue
                    if j + dj < 0:
                        continue
                    if i + di >= len(grid):
                        continue
                    if j + dj >= len(grid[0]):
                        continue
                    if visited[i + di][j + dj]:
                        continue
                    heapq.heappush(pq, (grid[i + di][j + dj], (i + di, j + dj)))
            memo[q] = count

        return [memo[x] for x in queries]
