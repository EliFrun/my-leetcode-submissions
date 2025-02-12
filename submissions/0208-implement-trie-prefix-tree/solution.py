class Trie:

    def __init__(self):
        self.head = [0, {}]

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if c not in curr[1]:
                curr[1][c] = [0, {}]
            curr = curr[1][c]
        curr[0] = 1   

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if c in curr[1]:
                curr = curr[1][c]
            else:
                return False
        
        return curr[0] == 1  

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if c in curr[1]:
                curr = curr[1][c]
            else:
                return False
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
