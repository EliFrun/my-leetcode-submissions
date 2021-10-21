class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            d = set()
            for i in row:
                if i != '.':
                    if i in d:
                        return False
                    else:
                        d.add(i)
            
        for i in range(9):
            d = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in d:
                        return False
                    else:
                        d.add(board[j][i])

            
        for i in range(3):
            for j in range(3):
                d = set()
                for k in range(3):
                    for l in range(3):
                        if board[3 * i + k][3 * j + l] != '.':
                            if board[3 * i + k][3 * j + l] in d:
                                return False
                            else:
                                d.add(board[3 * i + k][3 * j + l])

                
        return True
            
                    

        
