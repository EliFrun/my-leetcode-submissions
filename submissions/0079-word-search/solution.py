class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for a in enumerate(board):
            for b in enumerate(a[1]):
                if b[1] == word[0]:
                    ret = self.bfs(board, [(a[0], b[0])], word[1:])
                    if ret:
                        return ret
                    
        return False
                    
                
                    
                    
                    
                    
                    
    def bfs(self, board, visited, word):
        if not word:
            return True
        
        current_char = word[0]
        a = visited[-1]
        if (
            a[0] - 1 >= 0 and
            board[a[0] - 1][a[1]] == current_char and
            (a[0] - 1, a[1]) not in visited
        ):
            ret = self.bfs(board, visited + [(a[0] - 1, a[1])], word[1:])
            if ret:
                return ret
        if (
            a[1] - 1 >= 0 and
            board[a[0] ][a[1] - 1] == current_char and
            (a[0], a[1] - 1) not in visited
        ):
            ret = self.bfs(board, visited + [(a[0], a[1] - 1)], word[1:])
            if ret:
                return ret
        if (
            a[0] + 1 < len(board) and
            board[a[0] + 1][a[1]] == current_char and
            (a[0] + 1, a[1]) not in visited
        ):
            ret = self.bfs(board, visited + [(a[0] + 1, a[1])], word[1:])
            if ret:
                return ret
        if (
            a[1] + 1 < len(board[0]) and
            board[a[0]][a[1] + 1] == current_char and
            (a[0], a[1] + 1) not in visited
        ):
            ret = self.bfs(board, visited + [(a[0], a[1] + 1)], word[1:])
            if ret:
                return ret
        
        return False

                    
        
    
        
