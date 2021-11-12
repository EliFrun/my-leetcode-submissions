class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # problem simplifies to min distance to water
        ret = [[2000 for __ in range(len(isWater[0]))] for _ in range(len(isWater))]
        def bfs(curr):
            nonlocal ret
            visited = set()
            next_layer = set()
            curr_dis = 0
            found_next_water = False
            while curr:
                for i, j in curr: 
                    if (i, j) in visited:
                        continue
                    visited.add((i,j))
                    ret[i][j] = min(ret[i][j], curr_dis)
                    directions = [(-1, 0), (0, -1), (1,0), (0,1)]
                    for di, dj in directions:
                        if (0 <= i + di < len(isWater) and 0 <= j + dj < len(isWater[0]) and
                           (i + di, j + dj) not in visited
                           ):
                            next_layer.add((i + di, j + dj))
                        
                
                curr_dis += 1
                curr = next_layer
                next_layer = set()
        
        s = set()
        for i, row in enumerate(isWater):
            for j, val in enumerate(row):
                if val == 1:
                    s.add((i, j))
        
        bfs(s)
        
        return ret
                    
