class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # multi-bfs
        ret = [[0 for _ in range(len(mat[0]))] for __ in range(len(mat))]
        curr = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    curr.add((i,j))
        
        visited = set()
        layer = 0
        while curr:
            nxt = set()
            for i, j in curr:
                ret[i][j] = layer
                visited.add((i,j))
                dirs = [0, 1, 0, -1, 0]
                for m in range(4):
                    di = dirs[m]
                    dj = dirs[m + 1]
                    if i + di < 0 or i + di >= len(mat):
                        continue
                    if j + dj < 0 or j + dj >= len(mat[0]):
                        continue
                    if (i + di, j + dj) in visited:
                        continue
                    nxt.add((i + di, j + dj))
            curr = nxt.difference(visited)
            layer += 1

        return ret

        



