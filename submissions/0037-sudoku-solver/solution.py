class Solution:
    def valid_for_square(self, board, i, j):
        if board[i][j] != '.':
            return [board[i][j]]
        
        valid_values = set(list(range(1,10)))
        for row in range(9):
            if board[row][j] == '.':
                continue
            valid_values.discard(int(board[row][j]))
            
        for column in range(9):
            if board[i][column] == '.':
                continue
            valid_values.discard(int(board[i][column]))
            
        for x in range(3):
            for y in range(3):
                if board[3 * (i // 3) + x][3 * (j // 3) + y] == '.':
                    continue
                valid_values.discard(int(board[3 * (i // 3) + x][3 * (j // 3) + y]))
                
        return [str(x) for x in list(valid_values)]
    
    
    def solve(self, board):
        new_board = copy.deepcopy(board)
        updated = True
        while(updated):
            updated = False
            for i in range(9):
                for j in range(9):
                    if new_board[i][j] != '.':
                        continue
                    possible_values = self.valid_for_square(new_board, i, j)
                    if len(possible_values) == 0:
                        return []
                    if len(possible_values) == 1:
                        new_board[i][j] = possible_values[0]
                        updated = True
            
            
        # done updating
        # need to commit to values now
        for i in range(9):
            for j in range(9):
                possible_values = self.valid_for_square(new_board, i, j)
                if len(possible_values) >= 2:
                    for val in possible_values:
                        new_board[i][j] = val
                        tmp = self.solve(new_board)
                        if tmp != []:
                            return tmp
                    return []
        
        return new_board
                    
        
    
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        final_board = self.solve(board)
        for i in range(9):
            for j in range(9):
                board[i][j] = final_board[i][j]
        
