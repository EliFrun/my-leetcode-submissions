class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        next = copy.deepcopy(board)
        
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                lives = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k == i and l == j:
                            continue
                        if k < 0 or k > len(board) - 1:
                            continue
                        if l < 0 or l > len(board[0]) - 1:
                            continue
                        
                        lives += board[k][l]
                        
                if board[i][j] == 0:
                    next[i][j] = 1 if lives == 3 else 0
                else:
                    next[i][j] = 1 if lives == 2 or lives == 3 else 0
                    
                    
        for i, row in enumerate(next):
            for j, val in enumerate(row):
                board[i][j] = val
