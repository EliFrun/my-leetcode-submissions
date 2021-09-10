class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        foo = []
        for row in board:
            bar = []
            for s in row:
                bar.append(s)
            foo.append(bar)
            
        board = foo
        if self.solved(board, "O") and self.solved(board, "X"):
            return False
        a = self.count(board, "X") - self.count(board, "O")
        if a < 0 or a > 1:
            return False
        if self.solved(board, "O") and a != 0:
            return False
        if self.solved(board, "X") and a != 1:
            return False
        
        return True
        
    def count(self, board, v):
        c = 0
        for row in board:
            for value in row:
                if value == v:
                    c += 1
                    
        return c
    
    def solved(self, board, v):
        for i in range(3):
            if all(foo == v for foo in board[i]):
                return True
            
        for i in range(3):
            bar = []
            for j in range(3):
                bar.append(board[j][i])
            if all(foo == v for foo in bar):
                return True
        
        bar = []
        for i in range(3):
            bar.append(board[i][i])
        
        if all(foo == v for foo in bar):
                return True
            
        bar = []
        for i in range(3):
            bar.append(board[i][2 - i])
        
        if all(foo == v for foo in bar):
                return True
        
        return False
