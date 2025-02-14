class WordDictionary:

    def __init__(self):
        self.tr = [0, {}]
        

    def addWord(self, word: str) -> None:
        curr = self.tr
        for c in word:
            if c not in curr[1]:
                curr[1][c] = [0, {}]    
            curr = curr[1][c]

        curr[0] = 1
        

    def search(self, word1: str) -> bool:
        def solve(tr, word):
            for i, c in enumerate(word):
                if c == '.':
                    for  k in tr[1].keys():
                        if solve(tr[1][k], word[i + 1:]):
                            return True
                    return False
                if c in tr[1]:
                    tr = tr[1][c]
                else:
                    return False
            return tr[0] == 1
        return solve(self.tr, word1)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
