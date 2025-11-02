class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # scan the board 4 times
        ret = [[1] * n for _ in range(m)]
        guards = set([tuple(x) for x in guards])
        walls = set([tuple(x) for x in walls])
        curr = [1] * n
        for i in range(m):
            for j in range(n):
                if (i, j) in guards:
                    curr[j] = 0
                if (i, j) in walls:
                    curr[j] = 1
                ret[i][j] &=  curr[j]
        
        curr = [1] * n
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if (i, j) in guards:
                    curr[j] = 0
                if (i, j) in walls:
                    curr[j] = 1
                ret[i][j] &=  curr[j]


        curr = [1] * m
        for j in range(n):
            for i in range(m):
                if (i, j) in guards:
                    curr[i] = 0
                if (i, j) in walls:
                    curr[i] = 1
                ret[i][j] &=  curr[i]
        
        curr = [1] * m
        for j in range(n - 1, -1, -1):
            for i in range(m):
                if (i, j) in guards:
                    curr[i] = 0
                if (i, j) in walls:
                    curr[i] = 1
                ret[i][j] &=  curr[i]

        for i, j in guards:
            ret[i][j] = 0
        
        for i, j in walls:
            ret[i][j] = 0

        return sum(sum(x) for x in ret)

        
