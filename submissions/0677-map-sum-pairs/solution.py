class MapSum:

    def __init__(self):
        self.d = defaultdict(int)
        self.words = {}
        

    def insert(self, key: str, val: int) -> None:
        if key in self.words:
            for i in range(len(key) + 1):
                self.d[key[:i]] -= self.words[key]
        self.words[key] = val
        for i in range(len(key) + 1):
            self.d[key[:i]] += val

    def sum(self, prefix: str) -> int:
        return self.d[prefix]


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
