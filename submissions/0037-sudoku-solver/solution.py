class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        possibilities_matrix = [
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9,
            [[str(x) for x in range(1,10)]] * 9
        ]
        
        shortest_list = 1
        while shortest_list == 1:
            shortest_list = 10
            for row in enumerate(board):
                for column in enumerate(row[1]):
                    if column[1] == ".":
                        possibilities_matrix[row[0]][column[0]] = self.allValidValues(
                            board,
                            row[0],
                            column[0],
                            possibilities_matrix[row[0]][column[0]]
                        ) 
                        
                        shortest_list = min(shortest_list, len(possibilities_matrix[row[0]][column[0]]))
                        
                        if len(possibilities_matrix[row[0]][column[0]]) == 1:
                            board[row[0]][column[0]] = possibilities_matrix[row[0]][column[0]][0]

                    else:
                        possibilities_matrix[row[0]][column[0]] = []
        
        self.helper(board, possibilities_matrix)
        
                    
    
    
    def helper(self, board, p):
        possibilities_matrix = copy.deepcopy(p)
        while not self.solved(board):
            shortest_list = [x for x in range(11)]
            s_row, s_column = 0, 0
            for row in enumerate(board):
                for column in enumerate(row[1]):
                    if column[1] == ".":
                        if not possibilities_matrix[row[0]][column[0]]:
                            return
                        
                        if len(possibilities_matrix[row[0]][column[0]]) < len(shortest_list):
                            shortest_list = copy.deepcopy(possibilities_matrix[row[0]][column[0]])
                            s_row, s_column = row[0], column[0]
                        
                        if len(possibilities_matrix[row[0]][column[0]]) == 1:
                            board[row[0]][column[0]] = possibilities_matrix[row[0]][column[0]][0]
                            self.updateValues(possibilities_matrix, row[0], column[0], board[row[0]][column[0]])

                    else:
                        possibilities_matrix[row[0]][column[0]] = []
                        
                        
            if len(shortest_list) > 1:
                possibilities_matrix[s_row][s_column] = []
                for i in shortest_list:           
                    p = copy.deepcopy(possibilities_matrix)
                    self.updateValues(p, s_row, s_column, i)
                    
                    tmp_board = copy.deepcopy(board)
                    tmp_board[s_row][s_column] = i
                    
                    self.helper(tmp_board, p)
                    
                    if self.solved(tmp_board):
                        for row in range(9):
                            for column in range(9):
                                board[row][column] = tmp_board[row][column]
                        return
        
        
    def solved(self, board):
        for row in board:
            for column in row:
                if column == ".":
                    return False        
        return True
    
    
    def updateValues(self, p, row, column, value):
        self.updateRow(
            p,
            value,
            row,
        )
        self.updateColumn(
            p,
            value,
            column
        )
        self.updateBox(
            p,
            value,
            row // 3,
            column // 3,
        )
    
    def updateRow(self, p, value, row):
        for i in range(9):
            if value in p[row][i]:
                p[row][i].remove(value)
                
        
    def updateColumn(self, p, value, column):
        for i in range(9):
            if value in p[i][column]:
                p[i][column].remove(value)
    
    
    def updateBox(self, p, value, subbox_row, subbox_column):
        for i in range(3):
            for j in range(3):
                if value in p[3 * subbox_row + i][3 * subbox_column + j]:
                    p[3 * subbox_row + i][3 * subbox_column + j].remove(value)
    
    
    
    def allValidValues(self, board, row, column, options):
        ret = []
        for i in options:
            if (self.validInRow(board, row, i) and
                self.validInColumn(board, column, i) and
                self.validInSubbox(board, row//3, column//3, i)):
                ret.append(i)
        return ret
            
            
    def validInRow(self, board, row, number):
        for i in range(9):
            if board[row][i] == number:
                return False
        return True
        
        
    def validInColumn(self, board, column, number):
        for i in range(9):
            if board[i][column] == number:
                return False
        return True
        
    def validInSubbox(self, board, subbox_row, subbox_column, number):
        for i in range(3):
            for j in range(3):
                if board[3 * subbox_row + i][3 * subbox_column + j] == number:
                    return False
        return True
