class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def player_win(board):
            for i in range(3):
                if all([x != '.' and x == board[i][0] for x in board[i]]):
                    return True

            for i in range(3):
                eql = True
                for j in range(3):
                    if board[j][i] != board[0][i] or board[0][i] == '.':
                        eql = False
                        break
                if eql:
                    return True

            if all([board[0][0] != '.' and board[i][i] == board[0][0] for i in range(3)]):
                return True

            if all([board[0][2] != '.' and board[i][2 - i] == board[0][2] for i in range(3)]):
                return True

            return False

        board = [['.'] * 3 for _ in range(3)]
        for i, move in enumerate(moves):
            board[move[0]][move[1]] = 'X' if i % 2 == 0 else 'O'

        print(board)
        
        if player_win(board):
            return 'A' if len(moves) % 2 == 1 else 'B'
        
        return 'Draw' if len(moves) == 9 else 'Pending'

                
                    
        
