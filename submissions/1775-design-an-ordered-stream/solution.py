class OrderedStream:

    def __init__(self, n: int):
        self.lis = [None] * n
        self.idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lis[idKey - 1] = value
        ret = []
        while self.idx < len(self.lis) and self.lis[self.idx]:
            ret.append(self.lis[self.idx])
            self.idx += 1
        return ret


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
