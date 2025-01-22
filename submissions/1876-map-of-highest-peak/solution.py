class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ret = [[0 for j in range(len(isWater[0]))] for i in range(len(isWater))]

        curr = set()
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    curr.add((i,j))

        
        
        visited = set()
        nxt = set()
        layer = 0
        while len(curr) > 0:
            for i,j in list(curr):
                visited.add((i,j))
                ret[i][j] = layer
                if i - 1 >= 0 and (i - 1, j) not in visited:
                    nxt.add((i - 1, j))
                if j - 1 >= 0 and (i, j - 1) not in visited:
                    nxt.add((i, j - 1))
                if i + 1  < len(isWater) and (i + 1, j) not in visited:
                    nxt.add((i + 1, j))
                if j + 1 < len(isWater[0]) and (i, j + 1) not in visited:
                    nxt.add((i, j + 1))
            layer += 1
            curr = [x for x in nxt if x not in visited]
            nxt = set()

        return ret
    
