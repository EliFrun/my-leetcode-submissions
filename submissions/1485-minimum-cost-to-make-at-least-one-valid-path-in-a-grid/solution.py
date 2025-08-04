class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        costs = [[float('inf') for _ in range(len(grid[0]))] for __ in range(len(grid))]
        curr = [(0,0,0)]
        while curr:
            cost, x, y = heappop(curr)
            if cost >= costs[x][y]:
                continue
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return cost
            costs[x][y] = cost
            for i, (dx, dy) in enumerate([(0, 1), (0, -1), (1,0), (-1,0)]):
                dcost = 0 if i == grid[x][y] - 1 else 1
                if x + dx < 0 or x + dx >= len(grid) or y + dy < 0 or y + dy >= len(grid[0]):
                    continue
                if cost + dcost >= costs[x + dx][y + dy]:
                    continue
                heappush(curr, (cost + dcost, x + dx, y + dy))

        return 0
