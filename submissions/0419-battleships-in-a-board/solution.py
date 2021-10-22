class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        visited = set()
        def dfs(i, j):
            nonlocal visited
            if (i, j) in visited:
                return
            if board[i][j] != 'X':
                return
            visited.add((i, j))
            for di, dj in [(-1, 0), (0, -1), (1,0), (0,1)]:
                if 0 <= i + di < len(board) and 0 <= j + dj < len(board[0]):
                    dfs(i + di, j + dj)
                    
            
        ret = 0
        for i, row in enumerate(board):                    
            for j, v in enumerate(row):
                if v == 'X' and (i, j) not in visited:
                    ret += 1
                    dfs(i, j)
                    
        return ret
