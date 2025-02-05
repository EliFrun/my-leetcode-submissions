class StockSpanner:

    def __init__(self):
        self.prices = []
        self.i = 0
        

    def next(self, price: int) -> int:
        while self.prices and self.prices[-1][0] <= price:
            self.prices.pop()
        self.i += 1
        ret = (self.i - self.prices[-1][1] if self.prices else self.i)
        self.prices.append((price, self.i))
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
