class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # djikstras
        h = [(0,0,0)]
        dirs = [0,1,0,-1,0]
        while h:
            t, x, y = heappop(h)
            if x == len(moveTime) - 1 and y == len(moveTime[0]) - 1:
                return t
            if moveTime[x][y] < 0:
                continue
            moveTime[x][y] = -1
            for i in range(4):
                nx, ny = x + dirs[i], y + dirs[i + 1]
                if nx < 0 or ny < 0 or nx >= len(moveTime) or ny >= len(moveTime[0]):
                    continue
                if moveTime[nx][ny] >= 0:
                    heappush(h, (max(moveTime[nx][ny], t) + 1, nx, ny))


        return -1




                
                    
