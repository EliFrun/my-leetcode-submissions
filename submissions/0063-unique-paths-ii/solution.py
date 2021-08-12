class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                obstacleGrid[i][j] = -1 if obstacleGrid[i][j] == 1 else 0
        
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == -1:
                break
            else:
                obstacleGrid[i][0] = 1
        
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == -1:
                break
            else:
                obstacleGrid[0][i] = 1

        
        for i in range(1, min(len(obstacleGrid), len(obstacleGrid[0]))):
            for j in range(i, len(obstacleGrid[0])):
                if obstacleGrid[i][j] != -1:
                    if obstacleGrid[i][j - 1] != -1:
                       obstacleGrid[i][j] += obstacleGrid[i][j - 1]
                    if obstacleGrid[i - 1][j] != -1:
                       obstacleGrid[i][j] += obstacleGrid[i - 1][j]
            
            
            for j in range(i + 1, len(obstacleGrid)):
                if obstacleGrid[j][i] != -1:
                    if obstacleGrid[j][i - 1] != -1:
                       obstacleGrid[j][i] += obstacleGrid[j][i - 1]
                    if obstacleGrid[j - 1][i] != -1:
                       obstacleGrid[j][i] += obstacleGrid[j - 1][i]
                              
        return obstacleGrid[-1][-1]
