class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        marked_as_safe = set()
        
        for j, b in enumerate(board[0]):
            if b == "O":
                marked_as_safe.add((0, j))
                self.mark_squares(board, marked_as_safe, (0, j))
                
        for j, b in enumerate(board[-1]):
            if b == "O":
                marked_as_safe.add((len(board) - 1, j))
                self.mark_squares(board, marked_as_safe, (len(board) - 1, j))
                
        for i in range(1, len(board) - 1):
            if board[i][0] == "O":
                marked_as_safe.add((i, 0))
                self.mark_squares(board, marked_as_safe, (i, 0))
                
        for i in range(1, len(board) - 1):
            if board[i][len(board[0]) - 1] == "O":
                marked_as_safe.add((i, len(board[0]) - 1))
                self.mark_squares(board, marked_as_safe, (i, len(board[0]) - 1))
                
       
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in marked_as_safe:
                    board[i][j] = "X"
        
        
        
    def mark_squares(self, board, mark, coord):
        visiting = [coord]
        to_visit = []
        
        while visiting:
            for c in visiting:
                i, j = c[0], c[1]
                if i - 1 >= 0 and (i - 1, j) not in mark:
                    if board[i - 1][j] == "O":
                        mark.add((i - 1, j))
                        to_visit.append((i - 1, j))

                if j - 1 >= 0 and (i, j - 1) not in mark:
                    if board[i][j - 1] == "O":
                        mark.add((i, j - 1))
                        to_visit.append((i, j - 1))
                
                if i + 1 < len(board) and (i + 1, j) not in mark:
                    if board[i + 1][j] == "O":
                        mark.add((i + 1, j))
                        to_visit.append((i + 1, j))

                if j + 1 < len(board[0]) and (i, j + 1) not in mark:
                    if board[i][j + 1] == "O":
                        mark.add((i, j + 1))
                        to_visit.append((i, j + 1))
            
            visiting = to_visit
            to_visit = []


