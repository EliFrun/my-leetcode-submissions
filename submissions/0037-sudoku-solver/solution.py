class Solution:
    def solveSudoku(self, final_board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def valid_for_square(b, x, y):
            if b[x][y] != '.':
                return [b[x][y]]
            valid_values = set(list(range(1,10)))
            for i in range(0, 9):
                if b[x][i] != ".":
                    valid_values.discard(int(b[x][i]))

            for i in range(0, 9):
                if b[i][y] != ".":
                    valid_values.discard(int(b[i][y]))

            for i in range(3):
                for j in range(3):
                    if b[3 * (x // 3) + i][3 * (y // 3) + j] != ".":
                        valid_values.discard(int(b[3 * (x // 3) + i][3 * (y // 3) + j]))

            return [str(x) for x in valid_values]

        def solve(board):            
            next_board = copy.deepcopy(board)
            while (True):           
                test_board = copy.deepcopy(next_board)
                for i in range(9):
                    for j in range(9):
                        if next_board[i][j] != '.':
                            continue
                        possibilities = valid_for_square(next_board, i, j)
                        if len(possibilities) == 1:
                            next_board[i][j] = possibilities[0]
                        elif len(possibilities) == 0:
                            return []
                
                # reduce board to all forced values
                if all(test_board[i][j] == next_board[i][j] for i in range(9) for j in range(9)):
                    break
                
    
            
            # need to start committing to numbers
            for i in range(9):
                for j in range(9):
                    if next_board[i][j] == '.':
                        possibilities = valid_for_square(next_board, i, j)
                        if len(possibilities) > 1:
                            for val in possibilities:
                                next_board[i][j] = val
                                solution = solve(next_board)
                                if solution != []:
                                    return solution
                            return []
            
            
            # if above loop runs through all values and there all are not ".",
            # the board must be solved
            return next_board
                  
        
        solved = solve(final_board)
        
        for i in range(9):
            for j in range(9):
                final_board[i][j] = solved[i][j]
            
            
            
                                            
            
            
                                            
                                        
            
