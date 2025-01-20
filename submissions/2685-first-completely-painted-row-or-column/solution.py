class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        index_map = {}
        columns = defaultdict(int)
        rows = defaultdict(int)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                index_map[mat[i][j]] = (i, j)

        for i, v in enumerate(arr):
            columns[index_map[v][1]] += 1
            if columns[index_map[v][1]] == len(mat):
                return i

            rows[index_map[v][0]] += 1
            if rows[index_map[v][0]] == len(mat[0]):
                return i

        return len(arr)
        
