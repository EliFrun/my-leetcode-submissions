class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            curr = self.trie
            for i, c in enumerate(word):
                if c not in curr:
                    curr[c] = {}
                curr = curr[c] 
                if i == len(word) - 1:
                    curr['word'] = True
        self.ctx = []

    def query(self, letter: str) -> bool:
        self.ctx.append(self.trie)
        i = 0
        ret = False
        while i < len(self.ctx):
            if letter not in self.ctx[i]:
                self.ctx.pop(i)
                continue
            self.ctx[i] = self.ctx[i][letter]
            if 'word' in self.ctx[i]:
                ret = True
            i += 1

        return ret

            
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
