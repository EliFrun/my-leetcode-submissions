class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        class Trie:
            def __init__(self):
                self.root = {}

            def add(self, word):
                curr = self.root
                for c in word:
                    if c not in curr:
                        curr[c] = {}
                    curr = curr[c]
                curr['isWord'] = True

        def dfs(ret, t, word, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if not t:
                return
            if board[i][j] in t:
                t = t[board[i][j]]
            else:
                return
            word = word + board[i][j]
            if t.get('isWord'):
                ret.add(word)

            for di, dj in [(-1,0), (0,-1), (1,0), (0,1)]:
                original = board[i][j]
                board[i][j] = '-'
                dfs(ret, t, word, i + di, j + dj)
                board[i][j] = original
            return ret

        
        t = Trie()
        for word in words:
            t.add(word)
        
        ret = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(ret, t.root, '', i, j)

        return list(ret)

        
