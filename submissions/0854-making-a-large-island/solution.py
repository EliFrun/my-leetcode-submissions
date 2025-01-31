class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        explored = set()
        def bfs(i, j):
            curr = set([(i,j)])
            visited = set()
            boundary = set()
            while curr:
                nxt = set()
                steps = [(0,-1), (-1,0), (0,1), (1,0)]
                for i, j in curr:
                    visited.add((i,j))
                    for di, dj in steps:
                        if (i + di >= 0 and
                            i + di < len(grid) and
                            j + dj >= 0 and
                            j + dj < len(grid) and
                            (i + di, j + dj) not in visited):
                            if grid[i+di][j + dj] == 1:
                                nxt.add((i + di, j + dj))
                            else:
                                boundary.add((i + di, j + dj))

                curr = nxt

            return [visited, boundary]

        groups = {}
        candidates = set()
        group_coord_map = [[-1] * len(grid) for _ in range(len(grid))]
        group_num = 0
        zero_exists = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    zero_exists = True
                    continue
                if (i,j) in explored:
                    continue
                v, b = bfs(i, j)
                explored.update(v)
                candidates.update(b)
                groups[group_num] = v
                for x,y in v:
                    group_coord_map[x][y] = group_num

                group_num += 1

        if not zero_exists:
            return len(grid) * len(grid)
        #print(group_coord_map)
        ret = 1
        for i,j in candidates:
                if group_coord_map[i][j] != -1:
                    continue
                can_reach = set()
                steps = [(0,-1), (-1,0), (0,1), (1,0)]
                for di, dj in steps:
                    if (i + di >= 0 and
                        i + di < len(grid) and
                        j + dj >= 0 and
                        j + dj < len(grid)):
                            can_reach.add(group_coord_map[i + di][j + dj])

                can_reach = can_reach.difference(set([-1]))
                total = 1
                for v in can_reach:
                    total += len(groups[v])

                ret = max(total, ret)

        return ret
        

                    
        
